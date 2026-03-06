from collections.abc import Iterator

import pytest

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_key_value_unsafe import load_key_value_unsafe
from tests.create_key_value_table_if_not_exists_test import (
    setup_key_value_database,
)
from tests.execute_key_value_sql_test import delete_test_database_if_exists
from tests.key_types_test import BoolKeyForTesting, StrKeyForTesting

pytestmark = PYTEST_INTEGRATION_MARKER


@pytest.fixture(autouse=True)
def setup_and_teardown() -> Iterator[None]:
    setup_key_value_database()
    yield
    delete_test_database_if_exists()


def test_loads_key() -> None:
    arbitrary_key_1 = BoolKeyForTesting.BOOL_KEY_FOR_TESTING
    arbitrary_key_2 = StrKeyForTesting.STR_KEY_FOR_TESTING
    create_key(arbitrary_key_1, "True")
    create_key(arbitrary_key_2, "False")

    result1 = load_key_value_unsafe(arbitrary_key_1.value)
    result2 = load_key_value_unsafe(arbitrary_key_2.value)

    assert result1 == "True"
    assert result2 == "False"
