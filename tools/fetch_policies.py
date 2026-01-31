from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def fetch_policies(domain: str):
    """
    Fetch policy metadata for the given domain.
    Domain values are normalized for consistency.
    """

    # Normalize domain values
    domain_map = {
        "finance": "financial",
        "financial": "financial",
        "banking": "financial",
        "aml": "financial"
    }

    normalized_domain = domain_map.get(domain.lower())

    policies = []

    if not domain:
        domain = "financial"


    if normalized_domain == "financial":
        policies.append({
            "policy_id": "FATF_AML_2024",
            "title": "FATF AML Guidelines",
            "authority_level": "HIGH",
            "jurisdiction": "GLOBAL",
            "domain": "financial",
            "version": "2024.1",
            "effective_date": "2024-01-01",
            "source": "FATF",
            "knowledge_reference": "aml_policy_2024.txt"
        })

        policies.append({
            "policy_id": "FATF_AML_2025",
            "title": "FATF AML Guidelines",
            "authority_level": "HIGH",
            "jurisdiction": "GLOBAL",
            "domain": "financial",
            "version": "2025.1",
            "effective_date": "2025-01-01",
            "source": "FATF",
            "knowledge_reference": "aml_policy_2025.txt"
        })

    return {
        "policies": policies
    }
