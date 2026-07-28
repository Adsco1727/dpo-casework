from pathlib import Path

from dpo_ledger_tools import LedgerAPI

from dpo_casework import read_pending_clause_tasks


def test_can_read_pending_clause_queue_rows(tmp_path: Path):
    ledger_path = tmp_path / "operator_ledger.xlsx"
    ledger = LedgerAPI(ledger_path)
    ledger.ensure_exists()

    ledger.append_row(
        "CLAUSE_QUEUE",
        {
            "clause_task_id": "clause-001",
            "contract_id": "contract-a",
            "clause_engine": "Atticus",
            "analysis_type": "classification",
            "priority": 2,
            "status": "pending",
            "operator": "DPO",
            "notes": "seed",
        },
    )
    ledger.append_row(
        "CLAUSE_QUEUE",
        {
            "clause_task_id": "clause-002",
            "contract_id": "contract-b",
            "clause_engine": "ClauseX",
            "analysis_type": "deviation",
            "priority": 3,
            "status": "complete",
            "operator": "DPO",
            "notes": "seed",
        },
    )

    pending = read_pending_clause_tasks(ledger_path)
    assert len(pending) == 1
    assert pending[0]["clause_task_id"] == "clause-001"
