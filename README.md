<div align="center">

# KPI Intelligence-to-Action Engine

### Diagnoses why a KPI moved. Ranks the real drivers. Knows when it isn't sure.

**A deterministic KPI diagnostic engine with explainable, evidence-backed root-cause analysis**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq-8B5CF6?style=for-the-badge)](https://groq.com)
[![ChromaDB](https://img.shields.io/badge/RAG-ChromaDB-FFBE2E?style=for-the-badge)](https://www.trychroma.com/)
[![Status](https://img.shields.io/badge/Status-Working%20Prototype-4ADE80?style=for-the-badge)](https://github.com/dadhichmohak/kpi-intelligence-engine)

📦 **GitHub:** [github.com/dadhichmohak/kpi-intelligence-engine](https://github.com/dadhichmohak/kpi-intelligence-engine)

</div>

---

## 🎯 The Problem

Every retail business tracks KPIs across fragmented systems — different refresh cadences, inconsistent definitions, scattered data. When a number moves, the *why* lives somewhere else: warehouse tickets, CRM notes, field reports.

Most analytics tools stop at **"revenue dropped 18%."**

**Ours keeps going:** which department, driven by what, how confident are we, what should you do, and who should do it.

---

## 🔑 What Makes This Different

| Metric | Value |
|---|---|
| 🧮 **Deterministic core** | **100%** — every number from statistics, SQL, or retrieval |
| 🤖 **LLM calls** | **1** — narrative phrasing only, template fallback if unavailable |
| 📊 **Real transaction rows** | **421,570** |
| 🏬 **Stores / Departments** | **45 / 81** |
| ✅ **Demo scenarios** | **6** — all validated against real anomalies |
| 🔗 **Connected KPIs** | **5** — governed by YAML semantic contracts |

> The LLM is never the source of quantitative truth. That's not a limitation — **it's the design principle.**

---

## 🏗️ Architecture

```
  ┌─────────────────┐    ┌──────────────────┐    ┌────────────────┐    ┌────────────────────┐
  │ 📡 Signal Detect │───▶│ 🗄️ SQL Decompose  │───▶│ 🔍 Hybrid RAG  │───▶│ 🤖 Agent Orchestrate│
  │ (STL + controls) │    │ (pandas ranking) │    │ (BM25 + dense) │    │ (LangGraph ReAct)  │
  └─────────────────┘    └──────────────────┘    └────────────────┘    └─────────┬──────────┘
                                                                               │
  ┌─────────────────┐    ┌──────────────────┐    ┌────────────────┐           │
  │ 🔐 RBAC + Audit │◀───│ 💬 Narratives     │◀───│ ✅ Recommend    │◀──────────┘
  │ (5 roles)       │    │ (Groq + template)│    │ (4 templates)  │
  └─────────────────┘    └──────────────────┘    └────────────────┘
```

Every box is a real, tested code path — **not a diagram of intent.**

---

## 📂 Dataset Location

All data lives under `1_data_foundation/`:

```
1_data_foundation/
├── kpi_contract.yaml               # Single source of truth — formulas, thresholds, lineage, access rules
├── kpi_graph.yaml                  # KPI dependency graph + investigation traversal priority
├── sparse_history_registry.yaml    # Sparse store×dept combos + fallback strategies
├── dimensions/
│   ├── stores_dim.csv              # Static store metadata (Type A/B/C, Size/sqft)
│   └── store_region_mapping.csv    # Store-to-region assignment (North/South/East/West)
└── sources/
    ├── pos_weekly/
    │   └── sales_data.csv          # 421,570 rows — Store, Dept, Date, Weekly_Sales, IsHoliday
    ├── ops_weekly/
    │   └── features_data.csv       # Store-level markdowns, fuel price, CPI, unemployment
    └── field_reports_adhoc/
        └── field_reports.csv       # 79 curated tickets — CRM, warehouse, field reports
```

| File | Size | Records | Description |
|---|---|---|---|
| `sales_data.csv` | 12.6 MB | 421,570 | Weekly sales per store×dept (real retail data) |
| `features_data.csv` | 586 KB | ~6,400 | External factors: markdowns, fuel, CPI, unemployment |
| `field_reports.csv` | 15 KB | 79 | Curated operational tickets, access-tagged |

---

## ✅ Demo Scenarios

| # | Scenario | Store | What Happens | Confidence |
|---|---|---|---|---|
| 1 | 🔵 **Clean Single-Cause** | 18 | -52.9% drop ($606K). Weather-driven stockout. Evidence converges. | HIGH |
| 2 | 🟢 **Multi-Factor** | 27 | -25.7% drop ($523K). Supply hypothesis **refuted** by contradicting ticket. Real driver: promotional visibility. | HIGH |
| 3 | 🟡 **Abstention** | 17 | -23.9% drop ($254K). Evidence contradicts itself. System halts — no forced answer. | ABSTAIN |
| 4 | 🔠 **Sparse History** | 3/83 | One week of data. Cohort proxy from 14 peer stores. Confidence ceiling at 0.6. | MEDIUM |
| 5 | 🔠 **Sparse (No Baseline)** | 7/99 | Single test-batch. No valid peer group. System abstains entirely. | ABSTAIN |
| 6 | 🔒 **RBAC** | 41 | HR-sensitive tickets. Wrong region = denied. HR/Legal = full access. | HIGH |

> You can also investigate **any of the 45 stores** by typing the store ID manually — only these 6 have pre-validated demo scenarios with curated field reports.

---

## ⚙️ What's Deterministic vs. AI

| Phase | Component | Method | LLM? |
|:---:|---|---|:---:|
| 2 | Materiality detection | Statistical process control + STL decomposition | ❌ |
| 3 | Department decomposition | SQL-style contribution ranking | ❌ |
| 4 | Evidence retrieval | BM25 + sentence-transformer embeddings, RRF fusion | ❌ |
| 4 | Contradiction detection | Rule-based opposing-phrase heuristics | ❌ |
| 5 | Hypothesis ranking | Deterministic scoring (support − refutation + numeric weight) | ❌ |
| 6 | Confidence scoring | Agreement / match-strength / self-consistency, weighted | ❌ |
| 7 | Recommendations | Pre-approved action templates, slot-filled with real numbers | ❌ |
| 8 | **Persona narratives** | LLM phrasing of already-decided facts | ✅ |

> **100% deterministic core.** One LLM call exists — narrative synthesis — fact-constrained, with validated template fallback.

---

## 🚀 How to Run

### 1. Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Run all 6 demo scenarios (terminal)

```powershell
python -m 12_scenarios
```

Each scenario prints the full investigation trail — materiality, decomposition, evidence, hypothesis scoring, confidence, recommendation, and narratives.

### 3. Run the API + UI

```powershell
cd api
python main.py
```

Then open `ui/index.html` in your browser — it connects to `localhost:8000` automatically.

- Pick a scenario from the dropdown, or type any store ID (1-45)
- Click **Investigate** to run the full pipeline
- Swagger docs at `http://localhost:8000/docs`

### 4. Enable live LLM narratives (optional)

Create `.env` at project root:

```
GROQ_API_KEY=gsk_your_key_here
```

Without it, everything works — deterministic template narratives are used instead.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| 🎛️ **Orchestration** | LangGraph | ReAct-pattern state machine with conditional routing |
| 🔍 **Retrieval** | ChromaDB + sentence-transformers + BM25 | Hybrid RAG fused via Reciprocal Rank Fusion |
| 📈 **Statistics** | statsmodels + scipy | STL seasonal decomposition, control limits |
| 🤖 **LLM** | Groq (llama-3.3-70b) | Narrative synthesis only, template fallback |
| 🌐 **API** | FastAPI + uvicorn | REST endpoints with interactive /docs |
| 📊 **Data** | pandas + PyYAML | Semantic contracts, deterministic aggregation |
| 🐍 **Language** | Python 3.12 | Full codebase |

---

## 📁 Project Structure

```
├── 📂 1_data_foundation/      KPI contracts, dependency graph, sparse-history registry
│   ├── kpi_contract.yaml       Single source of truth (formulas, thresholds, lineage)
│   ├── dimensions/             Store metadata + region mapping
│   └── sources/                Real retail data (sales, operations, field reports)
├── 📂 2_signal_layer/          Statistical materiality detection (control limits + STL)
├── 📂 3_tools/                 SQL decomposition, contribution ranking, calculators
├── 📂 4_rag_layer/             Hybrid retrieval, contradiction detection
├── 📂 5_agent/                 LangGraph orchestrator, multi-hypothesis tracking
├── 📂 6_confidence_layer/      Agreement scoring, match strength, self-consistency
├── 📂 7_recommendation_engine/ Template-based action recommendations
├── 📂 8_narrative_layer/       Persona narratives (Groq LLM + template fallback)
├── 📂 9_feedback_loop/         Override capture, drift monitoring
├── 📂 10_security/             Role-based access enforcement (5 roles)
├── 📂 11_telemetry/            Latency logging, cost tracking, determinism ledger
├── 📂 12_scenarios/            6 validated demo scenarios
├── 📂 api/                     FastAPI REST endpoints
├── 📂 ui/                      Investigation console (single-file, no build)
├── 📂 docs/                    Business proposal, architecture diagram
├── 📄 .env.example             GROQ_API_KEY template
├── 📄 requirements.txt         33 Python dependencies
└── 📄 validate_data_foundation.py  YAML + column + sparse-history validation
```

---

## ⚠️ Known Limitations

| Limitation | Detail |
|---|---|
| 🔗 **Dataset-specific bindings** | Some modules reference this dataset's column names directly. Full parameterization is the next step toward dataset-agnostic deployment. |
| 🧠 **No causal inference** | Multi-hypothesis reasoning tests causes against evidence, but is not a formal causal model with counterfactuals. |
| 💬 **No free-text input** | Takes structured input (store, dept, week). Natural-language intent parsing is a planned extension. |
| 📉 **STL near minimum data** | The ~2.5-year dataset is near the minimum reliable window for seasonal decomposition. |

---

## 📝 Post Script

This project was built as a college capstone to demonstrate that **KPI diagnostics can be deterministic, honest, and actionable** — without making an LLM the authority on numbers it didn't compute.

### Design Decisions

- **LLM at the end, not the center.** Every number is earned by real statistics or retrieval before the language model ever sees it.
- **3-signal confidence scoring.** Agreement + match strength + self-consistency — weighted, not voted.
- **Proven determinism.** The telemetry ledger classifies all 14 pipeline steps. The claim is measured, not stated.
- **Graceful degradation.** Tested against a real API outage during development — the system kept working via template fallback.

### What Was Learned

- **Hybrid retrieval** (BM25 + dense embeddings) significantly outperforms either method alone for operational ticket search
- **Contradiction detection** changes recommendation quality more than improving retrieval
- **Abstention with explanation** is more valuable than a confident wrong answer
- **Deterministic-first** architecture makes debugging, auditing, and trust-building fundamentally easier

---

<div align="center">

📦 [github.com/dadhichmohak/kpi-intelligence-engine](https://github.com/dadhichmohak/kpi-intelligence-engine)

*KPI Intelligence-to-Action Engine*

</div>
