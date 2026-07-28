import pytest

from dpo_casework.errors import CaseworkPayloadError
from dpo_casework.payloads import validate_casework_payload


def test_can_validate_casework_payload():
    payload = {
        "clause_task_id": "clause-001",
        "analysis_type": "Scoring",
        "status": "Running",
        "reason_code": "RULE_MATCH",
        "operator": "DPO",
        "notes": "in review",
    }
    normalized = validate_casework_payload(payload)

    assert normalized["analysis_type"] == "scoring"
    assert normalized["status"] == "running"



def test_invalid_casework_payload_is_rejected():
    with pytest.raises(CaseworkPayloadError):
        validate_casework_payload(
            {
                "clause_task_id": "clause-001",
                "analysis_type": "unknown",
                "status": "running",
                "reason_code": "RULE_MATCH",
                "operator": "DPO",
            }
        )
