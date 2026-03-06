from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_bool import load_bool
from pl_key_value_sqlite_db.save_bool import save_bool
from tests.key_types_test import BoolKeyForTesting

ARBITRARY_BOOL_KEY = BoolKeyForTesting.BOOL_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_BOOL_KEY, "")


def test_save_and_load_bool__true() -> None:
    _set_up()

    save_bool(ARBITRARY_BOOL_KEY, True)
    result = load_bool(ARBITRARY_BOOL_KEY)

    assert result


def test_save_and_load_bool__false() -> None:
    _set_up()

    save_bool(ARBITRARY_BOOL_KEY, False)
    result = load_bool(ARBITRARY_BOOL_KEY)

    assert not result
