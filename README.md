# Phishing URL Processing Service

This service is responsible for fetching records from Google Sheets, processing the records to extract phishing URLs, and storing them in a MySQL database. Additionally, it provides error handling and status updates via Google Chat.

## Overview

- **Google Sheets Integration**: Fetches records from a Google Sheet.
- **MySQL Database**: Stores extracted phishing URLs and cluster names in a MySQL database.
- **Google Chat Integration**: Sends status messages about the processing of records and error messages if any occur.
  
## Requirements

- Python 3.x
- Google Sheets API credentials (for fetching records)
- Google Chat API credentials (for sending messages)
- MySQL Database

## Installation

### Without Docker

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    cd phishing-url-processing
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - `MYSQL_HOST`: The host of the MySQL database.
    - `MYSQL_USER`: The MySQL username.
    - `MYSQL_PASSWORD`: The MySQL password.
    - `MYSQL_DATABASE`: The MySQL database name.
    - Google API credentials (for Sheets and Chat).

### With Docker

1. Clone this repository to your local machine:
    ```bash
    git clone <repository-url>
    cd phishing-url-processing
    ```

2. Build and start the Docker container:
    ```bash
    docker build -t phishing-url-app .
    docker run -d --name phishing-url-app \
      -e MYSQL_HOST=mysql_host \
      -e MYSQL_USER=mysql_user \
      -e MYSQL_PASSWORD=mysql_password \
      -e MYSQL_DATABASE=mysql_database \
      -e GOOGLE_SHEET_CREDENTIALS=path_to_your_google_credentials \
      -e GOOGLE_CHAT_CREDENTIALS=path_to_your_google_chat_credentials \
      phishing-url-app
    ```

3. This will:
    - Build the Docker image.
    - Run the container with all necessary environment variables configured.

4. Set up your environment variables in the `docker run` command for Docker, including MySQL connection settings and Google API credentials.

## Configuration

### MySQL Database
- The service expects a MySQL database to be running and accessible with the provided credentials.
- The `PhishingURLModel` will store the following fields in the database:
  - `url`: The phishing URL.
  - `cluster_name`: The cluster name associated with the URL.

### Google Sheets
- The function `get_records` will fetch records from a Google Sheet. The data should include columns `URLs` and `Cluster Name`.

### Google Chat
- The `send_records_status_message` function sends a message to Google Chat indicating how many records were processed.
- The `send_error_message` function sends a message if an error occurs during the execution of the program.

## Running the Service

To run the service:

### Without Docker

1. Ensure all configurations (environment variables, Google API credentials, MySQL connection) are set correctly.
2. Run the main service:
    ```bash
    python app/main.py
    ```

### With Docker

If using Docker, you can simply run the container:

```bash
docker build -t phishing-url-app .
docker run -d --name phishing-url-app \
  -e MYSQL_HOST=mysql_host \
  -e MYSQL_USER=mysql_user \
  -e MYSQL_PASSWORD=mysql_password \
  -e MYSQL_DATABASE=mysql_database \
  -e GOOGLE_SHEET_CREDENTIALS=path_to_your_google_credentials \
  -e GOOGLE_CHAT_CREDENTIALS=path_to_your_google_chat_credentials \
  phishing-url-app
