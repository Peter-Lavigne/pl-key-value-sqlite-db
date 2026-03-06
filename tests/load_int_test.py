from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_int import load_int
from pl_key_value_sqlite_db.save_int import save_int
from tests.key_types_test import IntKeyForTesting

ARBITRARY_INT_KEY = IntKeyForTesting.INT_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_INT_KEY, "")


def test_save_and_load_int__positive() -> None:
    _set_up()

    save_int(ARBITRARY_INT_KEY, 42)
    result = load_int(ARBITRARY_INT_KEY)

    assert result == 42


def test_save_and_load_int__zero() -> None:
    _set_up()

    save_int(ARBITRARY_INT_KEY, 0)
    result = load_int(ARBITRARY_INT_KEY)

    assert result == 0


def test_save_and_load_int__negative() -> None:
    _set_up()

    save_int(ARBITRARY_INT_KEY, -15)
    result = load_int(ARBITRARY_INT_KEY)

    assert result == -15
