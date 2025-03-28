from app.services.google_chat.chat import send_error_message, send_records_status_message
from app.services.google_sheet.sheet import change_record_status, get_records
from app.services.my_sql.connection import create_mysql_connection
from app.services.my_sql.database import PhishingURLModel, insert_url
from app.utils import constants

def main():
    """
    Main function to call get_records and process the fetched records.
    """
    try:
        connection = create_mysql_connection()
        queue, count = get_records()

        while not queue.empty():
            record = queue.get()
            url_model = PhishingURLModel(
                url=record['URLs'],
                cluster_name=record['Cluster Name']
            )
            insert_url(connection, url_model)
        send_records_status_message(count)
        change_record_status()
    except Exception as e:
        send_error_message(str(e))
        constants.LOGGER.error(f"Error in main function: {e}")

if __name__ == "__main__":
    main()
