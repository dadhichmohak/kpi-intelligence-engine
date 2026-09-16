<div align="center">

# KPI Intelligence-to-Action Engine

### Diagnoses why a KPI moved. Ranks the real drivers. Knows when it isn't sure.

**A deterministic KPI diagnostic engine with explainable, evidence-backed root-cause analysis**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Groq](https://img.shields.io/badge/Groq-llama--3.3--70b-8B5CF6?style=for-the-badge)](https://groq.com)
[![Status](https://img.shields.io/badge/Status-Working%20Prototype-4ADE80?style=for-the-badge)](https://github.com/dadhichmohak/kpi-intelligence-engine)

</div>

---

## The Problem

Every retail business tracks KPIs across fragmented systems. When a number moves, the *why* lives somewhere else — warehouse tickets, CRM notes, field reports. Most tools stop at *"revenue dropped 18%."*

**Ours keeps going:** which department, driven by what, how confident are we, what should you do, and who should do it.

---

## What Makes This Different

| | |
|---|---|
| **Deterministic core** | **100%** — every number from statistics, SQL, or retrieval |
| **LLM calls** | **1** — narrative phrasing only, template fallback if unavailable |
| **Real data** | **421,570** transaction rows, 45 stores, 81 departments |
| **Demo scenarios** | **5 / 5** — all validated against real anomalies |
| **Connected KPIs** | **5** — governed by YAML semantic contracts |

> The LLM is never the source of quantitative truth. That's not a limitation — it's the design principle.

---

## Architecture

```
  Signal Detection ──> SQL Decomposition ──> Hybrid RAG ──> Agent Orchestration
       (stats)            (pandas)        (BM25+dense)       (LangGraph)
                                                                    │
  Feedback + Security <── Recommendations <── Confidence <──────────┘
       (RBAC)             (templates)        (3-signal scoring)
```

Every box is a real, tested code path — not a diagram of intent.

---

## Demo Scenarios

| # | Scenario | Store | What Happens |
|---|---|---|---|
| 1 | **Clean Single-Cause** | 18 | -52.9% drop. Weather stockout. Evidence converges. HIGH confidence. |
| 2 | **Multi-Factor** | 27 | -25.7% drop. Supply hypothesis **refuted** by contradicting ticket. Real driver: promotional visibility. |
| 3 | **Abstention** | 17 | -23.9% drop. Evidence contradicts itself. System halts — no forced answer. |
| 4 | **Sparse History** | 3/83 | One week of data. Cohort proxy from 14 peer stores. Confidence ceiling applied. |
| 5 | **RBAC** | 41 | HR-sensitive tickets. Wrong region = denied. Right role = full access. |

---

## How to Run

**1. Setup**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**2. Run scenarios (terminal)**

```powershell
python -m 12_scenarios
```

**3. Run API + UI**

```powershell
cd api
python main.py
```

Then open `ui/index.html` in your browser.

**4. Enable LLM narratives (optional)**

Create `.env` at project root:
```
GROQ_API_KEY=gsk_your_key_here
```

Without it, everything works — deterministic template narratives are used instead.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Orchestration | LangGraph (ReAct-pattern state machine) |
| Retrieval | ChromaDB + sentence-transformers + BM25, fused via RRF |
| Statistics | statsmodels (STL decomposition), custom control limits |
| LLM | Groq (llama-3.3-70b) — narrative synthesis only |
| API | FastAPI with interactive /docs |
| Data | pandas, YAML-governed semantic contracts |
| Language | Python 3.12 |

---

## Project Structure

```
1_data_foundation/      KPI contracts, dependency graph, sparse-history registry
2_signal_layer/         Statistical materiality detection (control limits + STL)
3_tools/                SQL decomposition, contribution ranking, calculators
4_rag_layer/            Hybrid retrieval, contradiction detection
5_agent/                LangGraph orchestrator, multi-hypothesis tracking
6_confidence_layer/     Agreement scoring, match strength, self-consistency
7_recommendation_engine/ Template-based action recommendations
8_narrative_layer/      Persona narratives (Groq LLM + template fallback)
9_feedback_loop/        Override capture, drift monitoring
10_security/            Role-based access enforcement (5 roles)
11_telemetry/           Latency logging, cost tracking, determinism ledger
12_scenarios/           5 validated demo scenarios
api/                    FastAPI REST endpoints
ui/                     Investigation console (single-file, no build)
docs/                   Business proposal, architecture diagram
```

---

## Known Limitations

| Limitation | Detail |
|---|---|
| **Dataset-specific bindings** | Some modules reference this dataset's column names directly. Full parameterization is the next step toward dataset-agnostic deployment. |
| **No causal inference** | Multi-hypothesis reasoning tests causes against evidence, but is not a formal causal model with counterfactuals. |
| **No free-text input** | Takes structured input (store, dept, week). Natural-language intent parsing is a planned extension. |
| **STL near minimum data** | The ~2.5-year dataset is near the minimum reliable window for seasonal decomposition. |

---

## Post Script

This project was built as a college capstone to demonstrate that **KPI diagnostics can be deterministic, honest, and actionable** — without making an LLM the authority on numbers it didn't compute.

The core insight: most "AI-powered analytics" tools either let a language model freestyle a plausible story, or build a rigid rules engine that can't handle nuance. This system does neither. It holds multiple hypotheses, actively looks for evidence that contradicts its own leading theory, downgrades that theory when it finds it, and abstains when the evidence doesn't support a confident answer.

**Key design decisions:**
- The LLM was deliberately placed at the *end* of the pipeline, not the center
- Every confidence score is a weighted combination of three independent signals
- The telemetry ledger proves the deterministic claim — it's not just stated, it's measured
- The system was tested against a real API outage during development and kept working via template fallback

**What was learned:**
- Hybrid retrieval (BM25 + dense embeddings) significantly outperforms either method alone for operational ticket search
- Contradiction detection changes the quality of recommendations more than improving retrieval
- An abstention policy that explains *why* it can't answer is more valuable than a confident wrong answer
- Deterministic-first architecture makes debugging, auditing, and trust-building fundamentally easier

The repository is public at [github.com/dadhichmohak/kpi-intelligence-engine](https://github.com/dadhichmohak/kpi-intelligence-engine).

---

<div align="center">

*KPI Intelligence-to-Action Engine*

</div>
