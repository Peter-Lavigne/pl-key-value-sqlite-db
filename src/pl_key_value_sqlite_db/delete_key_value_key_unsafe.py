from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import TABLE_NAME
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql


@MockInUnitTests(MockReason.UNINVESTIGATED)
def delete_key_value_key_unsafe(key: str) -> None:
    sql = f"""
        DELETE FROM {TABLE_NAME}
        WHERE key = ?
    """
    with execute_key_value_sql(sql, (key,)):
        pass
