# 📘 AegisAI (WatsonX Agentic AI Governance System)

---

## 🛡️ AegisAI — Governed Agentic AI for Policy-Aware Decision Making

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

AegisAI is composed of **five collaborating agents** and **four governed tools**, orchestrated using **IBM watsonx Orchestrate**.

### 🔹 Core Agents

1. **Intent & Risk Agent**
   - Classifies user intent and domain
   - Assigns risk level (LOW / MEDIUM / HIGH)
   - Distinguishes informational vs actionable requests

2. **Policy Intelligence Agent**
   - Retrieves all relevant policies from the knowledge base
   - Returns structured policy metadata (authority, version, date)

3. **Conflict Resolution Agent**
   - Detects conflicts and outdated policies
   - Computes a policy confidence score using weighted metrics:
     - Authority
     - Freshness
     - Agreement

4. **Governance Decision Agent**
   - Applies strict governance rules
   - Decides whether to:
     - RESPOND autonomously
     - ESCALATE for human review
     - REFUSE the request
   - Ensures human-in-the-loop enforcement

5. **Adaptive Learning Agent**
   - Handles policy evolution
   - Updates policy versions **only after human approval**
   - Never overwrites existing policies

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

### ✅ Scenario 1 — High-Risk Financial Action

**Query**  
> Can an AI system approve a high-value international financial transaction without human oversight?

**Outcome**
- **Decision:** ESCALATE  
- **Reason:** High risk + AML policy conflict  
- **Human review required**

---

### ✅ Scenario 2 — Informational Definition

**Query**  
> What is customer due diligence in financial systems?

**Outcome**
- **Decision:** RESPOND  
- **Reason:** Low-risk informational request  
- **High-level explanation only** (no procedural guidance)

---

### ✅ Scenario 3 — Compliance Bypass Attempt

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
