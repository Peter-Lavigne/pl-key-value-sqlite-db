from collections.abc import Iterator

import pytest

from pl_key_value_sqlite_db.constants import PYTEST_INTEGRATION_MARKER
from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.delete_key_value_key_unsafe import (
    delete_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.get_all_key_value_keys import get_all_key_value_keys
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


def test_deletes_key() -> None:
    arbitrary_key_1 = BoolKeyForTesting.BOOL_KEY_FOR_TESTING
    arbitrary_key_2 = StrKeyForTesting.STR_KEY_FOR_TESTING
    create_key(arbitrary_key_1, "True")
    create_key(arbitrary_key_2, "False")

    delete_key_value_key_unsafe(arbitrary_key_1.value)

    remaining_keys = get_all_key_value_keys()
    assert set(remaining_keys) == {arbitrary_key_2.value}
