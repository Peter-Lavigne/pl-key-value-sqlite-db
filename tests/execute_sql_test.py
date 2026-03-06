from collections.abc import Iterator
from pathlib import Path

import pytest
from pl_user_io.assert_yes import assert_yes

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.execute_sql import execute_sql

pytestmark = PYTEST_INTEGRATION_MARKER


def path_for_test_db() -> str:
    return "test.db"


def _remove_test_db_if_exists() -> None:
    path = Path(path_for_test_db())
    if path.exists():
        path.unlink()


def ready_env_for_test_database() -> None:
    _remove_test_db_if_exists()


def delete_test_database_if_exists() -> None:
    _remove_test_db_if_exists()


@pytest.fixture(autouse=True)
def setup_and_teardown() -> Iterator[None]:
    ready_env_for_test_database()
    yield
    delete_test_database_if_exists()


def test_database_file_is_created() -> None:
    assert not Path(path_for_test_db()).exists()

    with execute_sql("SELECT 1", path_for_test_db()):
        pass

    assert Path(path_for_test_db()).exists()


def test_can_execute_basic_sql() -> None:
    with execute_sql("SELECT 1", path_for_test_db()) as cursor:
        result = cursor.fetch_one()

        assert result == (1,)


def test_can_create_table_and_insert_data() -> None:
    with execute_sql(
        "CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);",
        path_for_test_db(),
    ):
        pass
    with execute_sql(
        "INSERT INTO test_table (name, age) VALUES ('Alice', 30), ('Bob', 25);",
        path_for_test_db(),
    ):
        pass

    with execute_sql(
        "SELECT COUNT(*) FROM test_table;", path_for_test_db()
    ) as response:
        result = response.fetch_one()

        assert result == (2,)


def test_can_fetch_one_row() -> None:
    with execute_sql(
        "CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);",
        path_for_test_db(),
    ):
        pass
    with execute_sql(
        "INSERT INTO test_table (name, age) VALUES ('Alice', 30), ('Bob', 25);",
        path_for_test_db(),
    ):
        pass

    with execute_sql(
        "SELECT * FROM test_table WHERE name = ?", path_for_test_db(), ("Alice",)
    ) as response:
        result = response.fetch_one()

        assert result == (1, "Alice", 30)


def test_can_fetch_all_rows() -> None:
    with execute_sql(
        "CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);",
        path_for_test_db(),
    ):
        pass
    with execute_sql(
        "INSERT INTO test_table (name, age) VALUES ('Alice', 30), ('Bob', 25);",
        path_for_test_db(),
    ):
        pass

    with execute_sql("SELECT * FROM test_table;", path_for_test_db()) as response:
        results = response.fetch_all()

        assert results == [(1, "Alice", 30), (2, "Bob", 25)]


def test_logs_sql_execution_readably() -> None:
    with execute_sql("SELECT 1", path_for_test_db()):
        pass

    assert_yes("Is there a log entry showing the executed SQL 'SELECT 1'?")
