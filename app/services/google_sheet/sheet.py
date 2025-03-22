import json
from datetime import datetime
from google.oauth2.service_account import Credentials
from queue import Queue
import gspread
from app.utils import config, constants

def initialize_google_sheet():
    """
    Initializes the Google Sheets client with the service account credentials.

    Returns:
        gspread.models.Worksheet: The first sheet of the Google Spreadsheet.
    
    Raises:
        Exception: If there is an error during initialization.
    """
    try:
        sheet_id = config.SHEET_ID
        # Create credentials object
        credentials = Credentials.from_service_account_info(config.google_creds, scopes=["https://www.googleapis.com/auth/spreadsheets"])
        # Initialize the Google Sheets client
        client = gspread.authorize(credentials)
        # Open the spreadsheet by ID
        workbook = client.open_by_key(sheet_id)
        sheet = workbook.sheet1 
        constants.LOGGER.info("Google Sheets initialized successfully")
        return sheet
    except Exception as e:
        raise Exception(f"Error initializing Google Sheets: {e}")
    
def get_records():
    """
    Fetches 50 records where is_completed is False and adds them to a queue.
    
    Args:
        sheet (gspread.models.Worksheet): The Google Sheets worksheet object.
    
    Returns:
        Queue: A queue containing up to 50 records.
    """
    try:
        sheet = initialize_google_sheet()
        # Find rows where 'is_completed' is False
        all_rows = sheet.get_all_values()  # Get all values, including headers
        header = all_rows[0]  # Assuming the first row is the header
        is_completed_col_index = header.index("is_completed")  # Find the column index of 'is_completed'

        queue = Queue()
        count = 0

        # Loop through rows starting from the second row (first is header)
        for row in all_rows[1:]:
            if row[is_completed_col_index].lower() == "false":  # Assuming 'False' is represented as a string
                # Map the row to a dictionary if needed
                record = dict(zip(header, row))
                queue.put(record)
                count += 1
                if count >= 50:
                    break
        
        constants.LOGGER.info(f"Added {count} records to the queue.")
        return queue, count
    except Exception as e:
        raise Exception(f"Error fetching pending records: {e}")
