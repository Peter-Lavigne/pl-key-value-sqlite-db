from types import NoneType

from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql

TABLE_NAME = "key_value"
KEY_COLUMN_NAME = "key"
VALUE_COLUMN_NAME = "value"


@MockInUnitTests(MockReason.UNINVESTIGATED)
def create_key_value_table_if_not_exists() -> NoneType:
    with execute_key_value_sql(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {KEY_COLUMN_NAME} TEXT NOT NULL UNIQUE,
            {VALUE_COLUMN_NAME} TEXT NOT NULL
        )
    """):
        pass
