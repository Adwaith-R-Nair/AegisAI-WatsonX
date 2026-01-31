from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def log_decision(
    user_query: str,
    decision: str,
    confidence: float,
    risk_level: str,
    policy_versions: list,
    reasoning_summary: str
):
    """
    Record a structured governance decision log entry.
    This log is used for auditability and transparency.
    """

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_query": user_query,
        "decision": decision,
        "final_confidence": confidence,
        "risk_level": risk_level,
        "policy_versions_considered": policy_versions,
        "reasoning_summary": reasoning_summary,
        "logged_by": "AegisAI Governance Engine"
    }

    # Return log entry for downstream observability / demo
    return {
        "status": "logged",
        "log_entry": log_entry
    }
