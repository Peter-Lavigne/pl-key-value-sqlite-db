from collections.abc import Iterator

import pytest

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.create_key_value_key_unsafe import (
    create_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import (
    KEY_COLUMN_NAME,
    TABLE_NAME,
    VALUE_COLUMN_NAME,
)
from pl_key_value_sqlite_db.execute_key_value_sql import execute_key_value_sql
from tests.create_key_value_table_if_not_exists_test import (
    setup_key_value_database,
)
from tests.execute_key_value_sql_test import delete_test_database_if_exists

pytestmark = PYTEST_INTEGRATION_MARKER


@pytest.fixture(autouse=True)
def setup_and_teardown() -> Iterator[None]:
    setup_key_value_database()
    yield
    delete_test_database_if_exists()


def test_creates_key_value_pair_with_default_value() -> None:
    create_key_value_key_unsafe("test_key", "test_value")

    with execute_key_value_sql(
        f"""
        SELECT {VALUE_COLUMN_NAME} FROM {TABLE_NAME}
        WHERE {KEY_COLUMN_NAME} = ?;
    """,
        ("test_key",),
    ) as cursor:
        result = cursor.fetch_one()

        assert result is not None
        assert result[0] == "test_value"
