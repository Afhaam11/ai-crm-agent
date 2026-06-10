# 🤖 AI CRM Agent — Natural Language Customer Analytics & Email Campaigns

An AI-powered CRM backend that lets you query customer data in plain English, generate personalized email campaigns, and track delivery — all driven by a LangChain ReAct agent powered by Groq's LLaMA model.

---

## ✨ Features

- 🔍 **Natural Language Querying** — Ask questions like *"Show me customers whose warranty expires in 30 days"* and get instant results
- 🧠 **LLM-Powered SQL Generation** — Automatically converts your question into safe DuckDB SQL queries
- 📧 **AI Email Campaign Generator** — Creates personalized email subject lines and body copy with `{{placeholder}}` support
- ✅ **Approval Workflow** — Campaigns are staged for review before sending — no accidental blasts
- 📊 **Audit Logging** — Every campaign and email delivery is logged to `.jsonl` files
- 🔁 **Duplicate Prevention** — SHA-256 hash tracking prevents sending the same email twice
- 📁 **Dynamic Excel Schema** — Works with any `.xlsx` file; auto-detects email and name columns
- 💬 **Conversation Context** — Follow-up queries are aware of previous questions in the session

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | [Groq](https://groq.com) — `llama-3.3-70b-versatile` |
| Agent Framework | [LangChain](https://langchain.com) ReAct Agent |
| Database | [DuckDB](https://duckdb.org) (in-memory) |
| Data Handling | Pandas + OpenPyXL |
| Email Sending | Python `smtplib` + Gmail SMTP |
| Environment | `python-dotenv` |
| Interface | Jupyter Notebook |

---

## 📁 Project Structure

```
CRM-Ai-main/
├── AI_CRM_Agent_Backend.ipynb   # Main notebook — all logic here
├── sales.xlsx                   # Sample customer data
├── campaign_audit_log.jsonl     # Auto-generated campaign audit trail
├── sent_emails_log.jsonl        # Auto-generated email delivery log
└── .env                         # Your secrets (not committed)
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/afhaam11/ai-crm-agent.git
cd ai-crm-agent
```

### 2. Install dependencies

```bash
pip install jupyter duckdb pandas openpyxl langchain langchain-groq langchain-core python-dotenv
```

### 3. Create a `.env` file or use `example.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
GMAIL_ADDRESS=youremail@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
```

> **Get a Groq API key:** Sign up free at [console.groq.com](https://console.groq.com)
>
> **Get a Gmail App Password:** 

### 4. Add your data

Place your customer Excel file (`.xlsx`) in the project root. The system auto-detects any column with "email" in its name. A sample `sales.xlsx` is included.

### 5. Launch Jupyter

```bash
jupyter notebook
```

Open `AI_CRM_Agent_Backend.ipynb` and run all cells.

---

## 🚀 Quick Start

```python
from AI_CRM_Agent_Backend import init_crm, query_customers_direct, create_campaign_direct, preview_email_direct, send_campaign_direct

# Initialize
crm = init_crm(
    org_name="Your Company",
    org_description="What your company does",
    excel_path="sales.xlsx"
)

# Query in plain English
results = query_customers_direct(crm, "Show me customers from Bangalore who bought Samsung TVs")

# Generate a campaign
campaign = create_campaign_direct(
    crm=crm,
    query="Samsung TV buyers in Bangalore",
    campaign_prompt="Offer them a 20% discount on extended warranty.",
    recipients=results['data']
)

# Preview before sending
preview = preview_email_direct(crm, campaign['campaign_id'], customer_index=0)
print(preview['subject'])
print(preview['body'])

# Send when ready
status = send_campaign_direct(crm, campaign['campaign_id'])
print(status)
```

---

## 🔄 Campaign Workflow

```
Query Customers  →  Generate Campaign  →  Preview Email  →  Approve  →  Send  →  Audit Log
```

Campaigns are always created in `pending_approval` status. You must explicitly call `send_campaign_direct()` or the agent's `approve_and_send_campaign` tool to trigger delivery.

---

## 🧰 Available Agent Tools

| Tool | Description |
|---|---|
| `query_customers` | Natural language → SQL → customer records |
| `get_schema_and_sample` | Inspect loaded data structure |
| `generate_email_campaign` | AI-generated subject + body for a recipient list |
| `preview_campaign` | Stage a manually written campaign |
| `preview_customer_email` | See personalized email for a specific customer |
| `approve_and_send_campaign` | Send a staged campaign |
| `get_campaign_status` | Check sent/failed/duplicate counts |
| `export_query_results` | Export last query to CSV, Excel, or JSON |
| `get_audit_logs` | Retrieve campaign and email delivery logs |

---

## 🔐 Security Notes

- Only `SELECT` queries are permitted — no `INSERT`, `UPDATE`, `DROP`, etc.
- `.env` is in `.gitignore` — never commit your API keys
- Email deduplication via SHA-256 hashing prevents accidental re-sends
- All campaign activity is append-only logged to `.jsonl` files

---

## 🙋‍♂️ Author

**Afhaam Ali**

AI/ML Engineer | LLM Agents & Intelligent Automation
