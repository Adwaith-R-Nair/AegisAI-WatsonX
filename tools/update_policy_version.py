from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def update_policy_version(
    previous_version: str,
    new_version: str,
    approved_by: str
):
    """
    Record a governed policy version update after explicit human approval.
    This does NOT modify policy content.
    It emits a versioning event for audit and governance.
    """

    version_update_event = {
        "event_type": "POLICY_VERSION_UPDATE",
        "timestamp": datetime.utcnow().isoformat(),
        "previous_version": previous_version,
        "new_active_version": new_version,
        "approved_by": approved_by,
        "status": "approved_and_active"
    }

    # Return event for auditability and observability
    return {
        "status": "policy_version_updated",
        "event": version_update_event
    }
