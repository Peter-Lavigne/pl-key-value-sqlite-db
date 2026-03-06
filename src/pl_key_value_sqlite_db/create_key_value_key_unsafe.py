from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import (
    KEY_COLUMN_NAME,
    TABLE_NAME,
    VALUE_COLUMN_NAME,
)
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql


@MockInUnitTests(MockReason.UNINVESTIGATED)
def create_key_value_key_unsafe(key: str, value: str) -> None:
    """
    Create a key in the database without type-safety.

    You should probably use key_value.create_key instead.
    """
    sql = f"""
        INSERT INTO {TABLE_NAME}
        ({KEY_COLUMN_NAME}, {VALUE_COLUMN_NAME})
        VALUES (?, ?)
    """
    with execute_key_value_sql(sql, (key, value)):
        pass
