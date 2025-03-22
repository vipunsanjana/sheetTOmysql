from app.utils import config, constants
import requests
from app.utils.constants import VALID_CONTENT_TYPE

def send_webhook_message(message: str):
    try:
        headers = {"Content-Type": VALID_CONTENT_TYPE}
        payload_text = {"text": message}
        response = requests.post(config.WEBHOOK_URL, json=payload_text, headers=headers)

        if response.status_code == 200:
            constants.LOGGER.info("Message sent successfully")
            return {"message": "Message sent successfully"}
        else:
            constants.LOGGER.error(f"Failed to send message, status code: {response.status_code}")
            raise Exception(f"Failed to send message, status code: {response.status_code}")
    except Exception as e:
        constants.LOGGER.error(f"Failed to send message: {e}")
        raise Exception(f"Failed to send message: {e}")

def send_records_status_message(records_inserted: int):
    message = f"✅ Successfully inserted {records_inserted} records into MySQL."
    send_webhook_message(message)

def send_error_message(error_message: str):
    message = f"❌ Error saving urls to database : {error_message}"
    send_webhook_message(message)
