from pl_mocks_and_fakes import mock_for

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped
from pl_key_value_sqlite_db.save_key_value_value_unsafe import (
    save_key_value_value_unsafe,
)
from tests.key_types_test import BoolKeyForTesting

ARBITRARY_KEY = BoolKeyForTesting.BOOL_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_KEY, "")


def test_loads_basekey_value() -> None:
    _set_up()
    mock_for(save_key_value_value_unsafe)("bool_key_for_testing", "True")

    result = load_value_untyped(ARBITRARY_KEY)

    assert result == "True"
