import json
import os
from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def update_policy_version(
    old_version: str,
    new_version: str
):
    """
    Update the active policy version after human approval.
    This simulates policy evolution in a governed system.
    """

    base_dir = os.path.dirname(os.path.dirname(__file__))
    metadata_path = os.path.join(
        base_dir,
        "data",
        "policies",
        "policy_metadata.json"
    )

    metadata = {
        "previous_version": old_version,
        "active_version": new_version,
        "updated_at": datetime.utcnow().isoformat(),
        "status": "policy_version_updated"
    }

    # Ensure directory exists
    os.makedirs(os.path.dirname(metadata_path), exist_ok=True)

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    return {
        "status": "policy_version_updated",
        "from": old_version,
        "to": new_version
    }
