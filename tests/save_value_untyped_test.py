from pl_mocks_and_fakes import mock_for

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_key_value_unsafe import load_key_value_unsafe
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped
from tests.key_types_test import BoolKeyForTesting

ARBITRARY_KEY = BoolKeyForTesting.BOOL_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_KEY, "")


def test_saves_basekey_value() -> None:
    _set_up()

    save_value_untyped(ARBITRARY_KEY, "True")

    assert mock_for(load_key_value_unsafe)("bool_key_for_testing") == "True"
