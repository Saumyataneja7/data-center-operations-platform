from databricks import sql
import pandas as pd

from config import (
    DATABRICKS_SERVER_HOSTNAME,
    DATABRICKS_HTTP_PATH,
    DATABRICKS_TOKEN
)


def execute_query(query: str):

    with sql.connect(
        server_hostname=DATABRICKS_SERVER_HOSTNAME,
        http_path=DATABRICKS_HTTP_PATH,
        access_token=DATABRICKS_TOKEN
    ) as connection:

        with connection.cursor() as cursor:

            cursor.execute(query)

            rows = cursor.fetchall()

            columns = [col[0] for col in cursor.description]

            return pd.DataFrame(rows, columns=columns)