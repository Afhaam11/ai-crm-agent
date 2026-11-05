import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

# ── API Keys ──────────────────────────────────────────────────────────────────
GROQ_API_KEY       = os.getenv("GROQ_API_KEY", "")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
FROM_EMAIL = os.getenv("FROM_EMAIL", "")

# ── LLM ───────────────────────────────────────────────────────────────────────
DEFAULT_MODEL   = "qwen/qwen3.8-27b"
LLM_TEMPERATURE = 0.0
LLM_MAX_TOKENS  = 1024

# ── Storage ───────────────────────────────────────────────────────────────────
AUDIT_LOG_PATH  = Path("crm_audit_log.jsonl")
SENT_EMAILS_LOG = Path("crm_sent_emails.jsonl")
EXPORT_DIR      = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)

# ── Query limits ──────────────────────────────────────────────────────────────
DEFAULT_QUERY_LIMIT = 500
MAX_QUERY_LIMIT     = 5000

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("ai_crm")

if not GROQ_API_KEY:
    logger.warning(" GROQ_API_KEY not set. LLM features will fail.")
else:
    logger.info("GROQ_API_KEY loaded.")
