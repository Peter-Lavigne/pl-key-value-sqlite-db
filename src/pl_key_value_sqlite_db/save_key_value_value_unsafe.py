from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import TABLE_NAME
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql


@MockInUnitTests(MockReason.UNINVESTIGATED)
def save_key_value_value_unsafe(key: str, value: str) -> None:
    """
    Set a value in the database by key without type-safety.

    You should probably use key_value.set_value instead.
    """
    sql = f"""
        UPDATE {TABLE_NAME}
        SET value = ?
        WHERE key = ?
    """
    with execute_key_value_sql(sql, (value, key)):
        pass
