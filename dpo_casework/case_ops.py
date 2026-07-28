"""Thin governed casework workflow operations backed by dpo-ledger-tools."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dpo_ledger_tools import LedgerAPI

from .payloads import validate_casework_payload


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_pending_clause_tasks(ledger_path: str | Path) -> list[dict[str, Any]]:
    ledger = LedgerAPI(ledger_path)
    rows = ledger.read_rows("CLAUSE_QUEUE")
    return [r for r in rows if str(r.get("status", "")).lower() == "pending"]


def write_casework_update(
    ledger_path: str | Path,
    payload: dict[str, Any],
    *,
    updated_at: str | None = None,
) -> dict[str, Any]:
    data = validate_casework_payload(payload)
    ledger = LedgerAPI(ledger_path)

    notes = f"reason_code={data['reason_code']}"
    if data["notes"]:
        notes = f"{notes} | {data['notes']}"

    updates = {
        "analysis_type": data["analysis_type"],
        "status": data["status"],
        "updated_at": updated_at or _utc_now_iso(),
        "operator": data["operator"],
        "notes": notes,
    }

    return ledger.update_row("CLAUSE_QUEUE", "clause_task_id", data["clause_task_id"], updates)
