from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_str import load_str
from pl_key_value_sqlite_db.save_str import save_str
from tests.key_types_test import StrKeyForTesting

ARBITRARY_STR_KEY = StrKeyForTesting.STR_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_STR_KEY, "")


def test_save_and_load_str() -> None:
    _set_up()
    s = "abc"

    save_str(ARBITRARY_STR_KEY, s)
    result = load_str(ARBITRARY_STR_KEY)

    assert result == s
