from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def create_escalation(
    user_query: str,
    triggered_rules: list,
    policy_version: str,
    severity: str = "high"
):
    """
    Create a human approval escalation payload.
    """

    escalation_payload = {
        "status": "pending_human_review",
        "timestamp": datetime.utcnow().isoformat(),
        "user_query": user_query,
        "triggered_rules": triggered_rules,
        "policy_version": policy_version,
        "severity": severity,
        "reason": "Regulatory policy requires human oversight"
    }

    return escalation_payload
