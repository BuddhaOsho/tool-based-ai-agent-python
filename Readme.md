# 🧠 AI Tool‑Calling CLI Agent (Python)

A command‑line AI agent built in Python that follows a structured **PLAN → TOOL → OBSERVE → OUTPUT** workflow.  
This project demonstrates how modern AI agents reason step‑by‑step, safely invoke external tools, and return **schema‑validated JSON outputs** instead of unstructured text.

---

## 🚀 Features

- ✅ **Agent‑Based Reasoning**
  - Implements structured thinking instead of free‑form responses
  - Inspired by real-world AI agent frameworks

- 🛠️ **Tool Calling Architecture**
  - Dynamically selects and executes tools based on model output
  - Easily extensible with new tools

- 📦 **Strict Output Validation**
  - Enforces deterministic JSON responses using **Pydantic**
  - Prevents malformed or unsafe LLM outputs

- 🌦️ **Live Weather Data**
  - Real‑time weather fetching using public APIs

- 💬 **Conversation Memory**
  - Maintains message history for contextual understanding

- 🔐 **Security‑Aware Design**
  - API keys managed via environment variables
  - Restricted system command execution

---



