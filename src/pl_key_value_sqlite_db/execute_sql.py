import logging
import sqlite3
from collections.abc import Callable, Generator
from contextlib import contextmanager
from typing import Any, NamedTuple

from pl_mocks_and_fakes import MockInUnitTests, MockReason


class ExecuteSqlResponse(NamedTuple):
    fetch_one: Callable[[], tuple[Any, ...] | None]
    fetch_all: Callable[[], list[tuple[Any, ...]]]


@MockInUnitTests(MockReason.UNINVESTIGATED)
@contextmanager
def execute_sql(
    sql: str, database_file_path: str, params: tuple[str, ...] = ()
) -> Generator[ExecuteSqlResponse]:
    conn = sqlite3.connect(
        database_file_path
    )  # Creates the DB file if it doesn't exist
    cursor = conn.cursor()
    logging.debug(f"Executing SQL:\n```\n{sql}\n```\nwith params: {params}")
    try:
        cursor.execute(sql, params)
        yield ExecuteSqlResponse(
            fetch_one=cursor.fetchone,
            fetch_all=cursor.fetchall,
        )
        conn.commit()
    finally:
        conn.close()
