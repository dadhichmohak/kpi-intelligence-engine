"""
llm_client.py
Thin wrapper around the Groq API (OpenAI-compatible) for Phase 8
narrative synthesis ONLY. This is deliberately the single place in
the entire codebase an LLM is called — every other phase (2-7, 9-12)
remains 100% deterministic.

Falls back gracefully: if no API key is set, or the call errors out
for any reason (network, rate limit, bad response), callers fall back
to the deterministic template narrative from persona_narrator.py.
The demo never breaks because of this layer.
"""

import os
import time
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

MODEL = "llama-3.3-70b-versatile"
MAX_TOKENS = 300
GROQ_BASE_URL = "https://api.groq.com/openai/v1"

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client

    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return None

    try:
        from openai import OpenAI
        _client = OpenAI(api_key=api_key, base_url=GROQ_BASE_URL)
        return _client
    except ImportError:
        return None


def is_llm_available() -> bool:
    return _get_client() is not None


def generate_persona_narrative(system_prompt: str, facts_prompt: str, step_name: str = "narrate_personas") -> dict:
    client = _get_client()
    if client is None:
        return {
            "success": False, "text": None,
            "input_tokens": 0, "output_tokens": 0, "latency_ms": 0,
            "error": "No LLM client available (missing GROQ_API_KEY or openai package).",
        }

    start = time.perf_counter()
    try:
        response = client.chat.completions.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.3,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": facts_prompt},
            ],
        )
        latency_ms = (time.perf_counter() - start) * 1000

        text = response.choices[0].message.content.strip()
        usage = response.usage

        return {
            "success": True, "text": text,
            "input_tokens": usage.prompt_tokens if usage else 0,
            "output_tokens": usage.completion_tokens if usage else 0,
            "latency_ms": round(latency_ms, 2),
            "error": None,
        }

    except Exception as e:
        latency_ms = (time.perf_counter() - start) * 1000
        return {
            "success": False, "text": None,
            "input_tokens": 0, "output_tokens": 0, "latency_ms": round(latency_ms, 2),
            "error": f"{type(e).__name__}: {e}",
        }


if __name__ == "__main__":
    print(f"LLM available: {is_llm_available()}")
    if is_llm_available():
        result = generate_persona_narrative(
            system_prompt="You rephrase structured business facts into one short, natural paragraph. Never add facts not given to you.",
            facts_prompt="Store: 18. Driver: Supply disruption. Action: Expedite restock. Confidence: HIGH.",
        )
        print(result)
    else:
        print("Set GROQ_API_KEY in .env to test the actual API call.")
