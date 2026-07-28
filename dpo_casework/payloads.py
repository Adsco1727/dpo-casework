"""Payload validation for governed casework actions."""

from __future__ import annotations

from typing import Any

from .errors import CaseworkPayloadError

ALLOWED_STATUS = {"pending", "running", "complete", "failed"}
ALLOWED_ANALYSIS_TYPES = {"classification", "deviation", "scoring", "fallback"}


def validate_casework_payload(payload: dict[str, Any]) -> dict[str, str]:
    required = ["clause_task_id", "analysis_type", "status", "reason_code", "operator"]
    missing = [field for field in required if not str(payload.get(field, "")).strip()]
    if missing:
        raise CaseworkPayloadError(f"missing required payload fields: {', '.join(missing)}")

    analysis_type = str(payload["analysis_type"]).strip().lower()
    if analysis_type not in ALLOWED_ANALYSIS_TYPES:
        raise CaseworkPayloadError(
            f"analysis_type must be one of {sorted(ALLOWED_ANALYSIS_TYPES)}; got '{payload['analysis_type']}'"
        )

    status = str(payload["status"]).strip().lower()
    if status not in ALLOWED_STATUS:
        raise CaseworkPayloadError(
            f"status must be one of {sorted(ALLOWED_STATUS)}; got '{payload['status']}'"
        )

    return {
        "clause_task_id": str(payload["clause_task_id"]).strip(),
        "analysis_type": analysis_type,
        "status": status,
        "reason_code": str(payload["reason_code"]).strip(),
        "operator": str(payload["operator"]).strip(),
        "notes": str(payload.get("notes", "")).strip(),
    }
