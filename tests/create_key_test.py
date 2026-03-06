from pl_mocks_and_fakes import mock_for

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_key_value_unsafe import load_key_value_unsafe
from tests.key_types_test import DateKeyForTesting

ARBITRARY_KEY = DateKeyForTesting.DATE_KEY_FOR_TESTING


def test_create_key() -> None:
    create_key(ARBITRARY_KEY, "test_value")

    assert mock_for(load_key_value_unsafe)(ARBITRARY_KEY.value) == "test_value"
