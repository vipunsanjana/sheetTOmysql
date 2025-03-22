import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Google Sheet URL
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")

# Google Chat Webhook URL
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Database Configuration
MYSQL_DB_HOST = os.getenv("MYSQL_DB_HOST")
MYSQL_DB_USER = os.getenv("MYSQL_DB_USER")
MYSQL_DB_PASSWORD = os.getenv("MYSQL_DB_PASSWORD")
MYSQL_DB_NAME = os.getenv("MYSQL_DB_NAME")
MYSQL_DB_PORT = os.getenv("MYSQL_DB_PORT")

private_key = os.getenv("GOOGLE_SHEETS_PRIVATE_KEY")
if private_key:
    private_key = private_key.replace(r"\n", "\n")  # This will replace the literal '\n' with actual newlines

google_creds = {
    "type": os.getenv("GOOGLE_SHEETS_TYPE"),
    "project_id": os.getenv("GOOGLE_SHEETS_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_SHEETS_PRIVATE_KEY_ID"),
    "private_key": private_key,  # Use the cleaned up private_key here
    "client_email": os.getenv("GOOGLE_SHEETS_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_SHEETS_CLIENT_ID"),
    "auth_uri": os.getenv("GOOGLE_SHEETS_AUTH_URI"),
    "token_uri": os.getenv("GOOGLE_SHEETS_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("GOOGLE_SHEETS_AUTH_PROVIDER_CERT_URL"),
    "client_x509_cert_url": os.getenv("GOOGLE_SHEETS_CLIENT_CERT_URL"),
    "universe_domain": os.getenv("GOOGLE_SHEETS_UNIVERSE_DOMAIN"),
}

# Google Sheet ID
SHEET_ID = os.getenv("SHEET_ID")

# List of all required environment variables
required_vars = [
    "MYSQL_DB_HOST",
    "MYSQL_DB_USER",
    "MYSQL_DB_PASSWORD",
    "MYSQL_DB_NAME",
    "MYSQL_DB_PORT",
    "SHEET_ID",
    "GOOGLE_SHEETS_TYPE",
    "GOOGLE_SHEETS_PROJECT_ID",
    "GOOGLE_SHEETS_PRIVATE_KEY_ID",
    "GOOGLE_SHEETS_PRIVATE_KEY",
    "GOOGLE_SHEETS_CLIENT_EMAIL",
    "GOOGLE_SHEETS_CLIENT_ID",
    "GOOGLE_SHEETS_AUTH_URI",
    "GOOGLE_SHEETS_TOKEN_URI",
    "GOOGLE_SHEETS_AUTH_PROVIDER_CERT_URL",
    "GOOGLE_SHEETS_CLIENT_CERT_URL",
    "GOOGLE_SHEETS_UNIVERSE_DOMAIN",
    "GOOGLE_SHEET_URL",
    "WEBHOOK_URL",
]

# Check for missing environment variables
missing_vars = [var_name for var_name in required_vars if not os.getenv(var_name)]

if missing_vars:
    raise ValueError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )