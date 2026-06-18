# BillSense AI 🧾
**Smart Invoice Processing Engine powered by Local AI & n8n**

BillSense is an automated, enterprise-grade financial auditor built to process commercial invoices with zero manual data entry and zero cloud API costs. It uses local LLMs to extract unstructured data, runs deterministic compliance checks, converts global currencies to INR in real-time, and logs everything autonomously.

##  Core Features
* **Zero-Cost Local AI Extraction:** Uses Llama 3.1 (via Ollama) to read PDFs and perfectly structure vendor data, invoice numbers, and line items without sending sensitive financial documents to third-party cloud APIs.
* **Deterministic Fraud Auditing:** Bypasses LLM logic hallucinations by using hard-coded JavaScript nodes to run strict tax compliance checks (e.g., flagging invoices that charge GST but fail to provide a valid GSTIN).
* **Live Global Currency Conversion:** Automatically detects foreign currencies (USD, EUR, AUD, etc.) and pings a live exchange rate API to standardize all logged financial data into INR.
* **Full-Loop Automation:** Validated data is automatically appended to Google Sheets, and email summaries are routed via Gmail, all while passing dynamic success/failure alerts back to the Streamlit UI.

##  Tech Stack
* **Frontend:** Python, Streamlit
* **Backend Automation:** n8n (Node-based workflow architecture)
* **AI Engine:** Ollama (Local Llama 3.1 8B Model)
* **External APIs:** Open Exchange Rates (er-api), Google Workspace APIs

---

## 🚀 Installation & Setup

### Prerequisites
1. **[Ollama](https://ollama.com/)** installed locally with the Llama 3.1 model (`ollama pull llama3.1`).
2. **[n8n](https://n8n.io/)** installed and running locally or via Docker.
3. **Python 3.9+** installed.

### Step 1: Clone the Repository
```bash
git clone [https://github.com/KaustubhOps27/billsense-invoice-agent.git](https://github.com/KaustubhOps27/billsense-invoice-agent.git)
cd BillSense
