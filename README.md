#  AegisAI (WatsonX Agentic AI Governance System)

---

## 🛡️ AegisAI : Governed Agentic AI for Policy-Aware Decision Making

AegisAI is an **agentic AI governance system** built using **IBM watsonx.ai and watsonx Orchestrate**, designed to ensure that AI systems make decisions that are **policy-compliant, explainable, auditable, and human-aligned**.

Instead of treating AI as a single black-box model, AegisAI orchestrates **multiple specialized agents** that collaboratively analyze intent, retrieve policies, detect conflicts, compute confidence, and decide **when AI can act autonomously and when human oversight is mandatory**.

This project was developed as part of the  
**IBM Agentic AI Dev Day – watsonx & IBM Challenge Hackathon**.

---

## 🚨 Problem Statement

Modern AI systems are increasingly used in **regulated and high-risk domains** such as finance, healthcare, governance, and compliance.

However, most AI systems today:

- make decisions without explicit policy grounding  
- cannot explain *why* a decision was allowed or blocked  
- lack confidence calibration  
- fail to enforce human-in-the-loop controls  
- silently drift when policies change  

This creates serious risks in:

- regulatory compliance (AML, KYC, FATF, etc.)
- accountability and auditability
- trust and adoption of AI in enterprises

---

## 💡 Our Solution

**AegisAI** introduces a **governance-first agentic architecture** where:

- AI **does not act blindly**
- Policies are **explicitly retrieved and versioned**
- Conflicts between policies are **detected and scored**
- Confidence is **computed, not guessed**
- High-risk decisions are **automatically escalated to humans**
- Informational queries are handled safely without over-restriction
- Policy evolution happens **only with human approval**

> **AegisAI knows when to act, when to stop, and when to ask a human.**

---

## 🧠 System Architecture (High-Level)

## 🔁 Agentic AI Orchestration Flow

AegisAI follows a deterministic, multi-agent governance workflow orchestrated using IBM watsonx Orchestrate:

1. **Intent & Risk Agent**
   - Analyzes the user query
   - Classifies intent, domain, and risk level

2. **Policy Intelligence Agent**
   - Retrieves all relevant policy documents from the knowledge base
   - Returns structured metadata without interpretation

3. **Conflict Resolution Agent**
   - Evaluates policy consistency, authority, and freshness
   - Computes a policy confidence score using weighted metrics

4. **Governance Decision Agent**
   - Applies governance rules based on risk, conflicts, and confidence
   - Decides whether to RESPOND, ESCALATE, or REFUSE
   - Enforces human-in-the-loop where required

5. **Adaptive Learning Agent**
   - Handles policy evolution after explicit human approval
   - Ensures versioned, auditable updates without overwriting history

This separation of concerns ensures explainability, auditability, and safe autonomy.

---

### 🔹 Governed Tools

- **fetch_policies**
  - Returns policy metadata for a given domain

- **create_escalation**
  - Generates structured human-review escalation payloads

- **log_decision**
  - Records every decision with reasoning for auditability

- **update_policy_version**
  - Emits policy version update events after approval

---

## 📊 Confidence Scoring Logic

AegisAI computes **policy confidence**, not answer confidence.

Confidence reflects:
- clarity of policy authority
- recency of policies
- agreement between policies

### Formula

```text
confidence_score =
(authority_score × 0.4) +
(freshness_score × 0.3) +
(agreement_score × 0.3)
```

⚠️ **Important**

A high confidence score does **not** automatically allow autonomous action.  
Risk level and governance rules can still force escalation.

---

## 🧪 Verified Scenarios

### ✅ Scenario 1 : High-Risk Financial Action

**Query**  
> Can an AI system approve a high-value international financial transaction without human oversight?

**Outcome**
- **Decision:** ESCALATE  
- **Reason:** High risk + AML policy conflict  
- **Human review required**

---

### ✅ Scenario 2 : Informational Definition

**Query**  
> What is customer due diligence in financial systems?

**Outcome**
- **Decision:** RESPOND  
- **Reason:** Low-risk informational request  
- **High-level explanation only** (no procedural guidance)

---

### ✅ Scenario 3 : Compliance Bypass Attempt

**Query**  
> Can we skip enhanced due diligence for a high-risk customer?

**Outcome**
- **Decision:** ESCALATE  
- **Reason:** Direct violation of FATF AML requirements

---

## 🏗️ Project Structure

```text
AegisAI-WatsonX/
├── agents/
│   ├── intent_risk_agent.yaml
│   ├── policy_intelligence_agent.yaml
│   ├── conflict_resolution_agent.yaml
│   ├── governance_decision_agent.yaml
│   └── adaptive_learning_agent.yaml
│
├── tools/
│   ├── fetch_policies.py
│   ├── create_escalation.py
│   ├── log_decision.py
│   └── update_policy_version.py
│
├── knowledge/
│   ├── aml_policy_2024.txt
│   └── aml_policy_2025.txt
│
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- **IBM watsonx.ai**
- **IBM watsonx Orchestrate**
- **Agentic AI architecture**
- **Python (governed tools)**
- **Policy-driven AI design**
- **Human-in-the-loop governance**

---

## 👥 Team

- **Milan** : Agent Orchestration & Flow Design  
- **Mahathi** : Tools & Backend Engineering  
- **Adwaith R Nair** : watsonx.ai, Prompt Design & Reasoning Logic  
- **Meenakshi** : Frontend, Documentation & Demo  

---

## 🏁 Conclusion

AegisAI demonstrates how **agentic AI systems can be governed responsibly** in real-world, high-risk environments.

By combining:
- structured reasoning  
- explicit policy grounding  
- confidence-aware decisions  
- human oversight  
- and versioned learning  

AegisAI moves beyond *“AI that answers”* to  
**AI that knows when it should not.**

---

## 📌 License & Disclaimer

This project is a **hackathon prototype** created for educational and demonstration purposes.  
It is **not intended for production deployment without further validation and compliance review**.
