from collections.abc import Generator
from contextlib import contextmanager

from pl_mocks_and_fakes import MockInUnitTests, MockReason

from pl_key_value_sqlite_db.execute_sql import ExecuteSqlResponse, execute_sql
from pl_key_value_sqlite_db.settings import get_settings


@MockInUnitTests(MockReason.UNINVESTIGATED)
@contextmanager
def execute_key_value_sql(
    sql: str, params: tuple[str, ...] = ()
) -> Generator[ExecuteSqlResponse]:
    with execute_sql(sql, get_settings().key_value_db_path, params) as cursor:
        yield cursor
