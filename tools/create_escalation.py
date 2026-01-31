from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def create_escalation(
    user_query: str,
    decision_confidence: float,
    risk_level: str,
    policy_versions: list,
    escalation_reason: str
):
    """
    Create a human-in-the-loop escalation payload
    based on governance decision outcomes.
    """

    escalation_payload = {
        "status": "pending_human_review",
        "timestamp": datetime.utcnow().isoformat(),
        "user_query": user_query,
        "decision_confidence": decision_confidence,
        "risk_level": risk_level,
        "policy_versions_considered": policy_versions,
        "escalation_reason": escalation_reason,
        "source": "AegisAI Governance Engine"
    }

    return escalation_payload
