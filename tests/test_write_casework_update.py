from pathlib import Path

from dpo_ledger_tools import LedgerAPI

from dpo_casework import write_casework_update


def test_can_write_deterministic_clause_queue_update(tmp_path: Path):
    ledger_path = tmp_path / "operator_ledger.xlsx"
    ledger = LedgerAPI(ledger_path)
    ledger.ensure_exists()

    ledger.append_row(
        "CLAUSE_QUEUE",
        {
            "clause_task_id": "clause-100",
            "contract_id": "contract-z",
            "clause_engine": "HermesLegal",
            "analysis_type": "classification",
            "priority": 1,
            "status": "pending",
            "operator": "DPO",
            "notes": "seed",
        },
    )

    result = write_casework_update(
        ledger_path,
        {
            "clause_task_id": "clause-100",
            "analysis_type": "scoring",
            "status": "running",
            "reason_code": "RULE_MATCH",
            "operator": "DPO",
            "notes": "executing casework",
        },
        updated_at="2026-07-28T16:00:00Z",
    )

    assert result["analysis_type"] == "scoring"
    assert result["status"] == "running"
    assert result["updated_at"] == "2026-07-28T16:00:00Z"
    assert "reason_code=RULE_MATCH" in result["notes"]
