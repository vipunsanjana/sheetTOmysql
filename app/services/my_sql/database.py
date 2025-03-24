from mysql.connector import Error
from typing import Optional
from app.utils import constants
from pydantic import BaseModel

class PhishingURLModel(BaseModel):
    url: str
    cluster_name: str

def execute_query(connection, query: str, values: Optional[tuple] = None, fetch: bool = False):
    """
    Execute a SQL query with optional values and fetch result if required.
    
    Args:
        connection: Active database connection.
        query (str): SQL query string.
        values (tuple, optional): Values to be inserted into the query.
        fetch (bool, optional): Whether to fetch results. Defaults to False.

    Returns:
        List[tuple]: List of results if fetch is True, else None.
    Raises:
        Error: If there is an error executing the query.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values) if values else cursor.execute(query)
            if fetch:
                return cursor.fetchall()
            connection.commit()
            constants.LOGGER.info("Query executed successfully.")
    except Error as e:
        connection.rollback()
        constants.LOGGER.error(f"Database query error: {e}")
        raise Exception(f"Database query error: {e}")

class PhishingQueries:
    INSERT_URL = """
        INSERT INTO phishing_url_tracking 
        (url, cluster_name) 
        VALUES (%s, %s)
    """

def insert_url(connection, url: PhishingURLModel):
    """
    Inserts a phishing URL and its associated cluster name into the database.
    
    Args:
        connection: Active database connection.
        url (PhishingURLModel): The phishing URL model containing the URL and cluster name.
    """
    values = (url.url, url.cluster_name)
    execute_query(connection, PhishingQueries.INSERT_URL, values)
