import os
from collections.abc import Iterator
from pathlib import Path

import pytest

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql

pytestmark = PYTEST_INTEGRATION_MARKER


def path_for_test_db() -> str:
    return "test.db"


def _remove_test_db_if_exists() -> None:
    path = Path(path_for_test_db())
    if path.exists():
        path.unlink()


def ready_env_for_test_database() -> None:
    os.environ["KEY_VALUE_DB_PATH"] = path_for_test_db()
    _remove_test_db_if_exists()
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

    with execute_key_value_sql("SELECT 1"):
        pass

    assert Path(path_for_test_db()).exists()
