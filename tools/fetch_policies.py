import json
import os
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def fetch_policies(domain: str, version: str = "2025"):
    """
    Fetch AML policy rules for a given domain and version.
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    policy_path = os.path.join(
        base_dir,
        "data",
        "policies",
        f"aml_policy_{version}.json"
    )

    if not os.path.exists(policy_path):
        return []

    with open(policy_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if data.get("domain") != domain:
        return []

    return data.get("rules", [])
