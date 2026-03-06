from datetime import date

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_date import load_date
from pl_key_value_sqlite_db.save_date import save_date
from tests.key_types_test import DateKeyForTesting

ARBITRARY_DATE_KEY = DateKeyForTesting.DATE_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_DATE_KEY, "")


def test_save_and_load_date() -> None:
    _set_up()
    d = date(2000, 1, 1)

    save_date(ARBITRARY_DATE_KEY, d)
    result = load_date(ARBITRARY_DATE_KEY)

    assert result == d
