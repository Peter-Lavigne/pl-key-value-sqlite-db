from collections.abc import Iterator

import pytest

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import (
    TABLE_NAME,
    create_key_value_table_if_not_exists,
)
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql
from tests.execute_key_value_sql_test import (
    delete_test_database_if_exists,
    ready_env_for_test_database,
)

pytestmark = PYTEST_INTEGRATION_MARKER


def setup_key_value_database() -> None:
    ready_env_for_test_database()
    create_key_value_table_if_not_exists()


@pytest.fixture(autouse=True)
def setup_and_teardown() -> Iterator[None]:
    ready_env_for_test_database()
    yield
    delete_test_database_if_exists()


def test_create_key_value_table_if_not_exists_creates_table() -> None:
    create_key_value_table_if_not_exists()

    with execute_key_value_sql(f"""
        SELECT name FROM sqlite_master WHERE type='table' AND name='{TABLE_NAME}';
    """) as cursor:
        result = cursor.fetch_one()

        assert result is not None
        assert result[0] == TABLE_NAME


def test_create_key_value_table_if_not_exists_does_not_cause_error_on_rerun() -> None:
    create_key_value_table_if_not_exists()
    create_key_value_table_if_not_exists()
