import logging

from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import TABLE_NAME
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql


@MockInUnitTests(MockReason.UNINVESTIGATED)
def load_key_value_unsafe(key: str) -> str:
    """
    Get a value in the database by key without type-safety.

    You should probably use key_value.get_value instead.
    """
    sql = f"""
        SELECT value
        FROM {TABLE_NAME}
        WHERE key = ?
    """
    with execute_key_value_sql(sql, (key,)) as cursor:
        result = cursor.fetch_one()
        assert result is not None, f"Key '{key}' not found in database."
        result_value = result[0]
        logging.debug(f"Returned value: {result_value}")
        return result_value
