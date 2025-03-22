import logging

# Logging
logging.basicConfig(
    level=getattr(logging, "INFO", logging.INFO),
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Logger
LOGGER = logging.getLogger(__name__)

# web page content types
VALID_CONTENT_TYPE = "application/json"
