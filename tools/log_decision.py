import json
import os
from datetime import datetime
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def log_decision(
    user_query: str,
    decision: str,
    rule_ids: list,
    policy_version: str
):
    """
    Append an audit log entry for every agent decision.
    """

    base_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base_dir, "logs")
    log_path = os.path.join(log_dir, "decision_log.jsonl")

    # Ensure logs directory exists
    os.makedirs(log_dir, exist_ok=True)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_query": user_query,
        "decision": decision,
        "rules_triggered": rule_ids,
        "policy_version": policy_version
    }

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {"status": "logged"}
