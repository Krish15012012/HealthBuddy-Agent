# HealthBuddy: The Medical Translator Agent 🩺
### Capstone Submission for AI Agents Course

**Track:** Agents for Good

## 💡 The Problem
Medical reports are confusing. Patients see terms like "Leukocytosis" or "Hyperlipidemia" and get scared. They struggle to understand their own health data.

## 🤖 The Solution
HealthBuddy is a **Multi-Agent System** that simplifies medical jargon into 5th-grade English.
1.  **Analyst Agent:** Scans the text to identify complex terms.
2.  **Medical Tool:** Searches the web (DuckDuckGo) for verified medical definitions.
3.  **Translator Agent:** Rewrites the report using the verified data.

## 🛠️ Architecture & Concepts Used
* **Multi-Agent Orchestration:** Sequential flow (Analyst -> Translator).
* **Tooling:** Integrated web search tool for grounding facts.
* **Memory:** Uses Session State to remember conversation history.
* **Model:** Powered by Gemini 1.5 Flash.

## 🚀 How to Run
1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Add your Gemini API Key in a `.env` file.
4.  Run: `streamlit run app.py`
