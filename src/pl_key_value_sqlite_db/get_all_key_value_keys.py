import logging

from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import TABLE_NAME
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql


@MockInUnitTests(MockReason.UNINVESTIGATED)
def get_all_key_value_keys() -> list[str]:
    sql = f"""
        SELECT key
        FROM {TABLE_NAME}
    """
    with execute_key_value_sql(sql) as cursor:
        result = [row[0] for row in cursor.fetch_all()]
        logging.debug(f"Returned value: {result}")
        return result
