from datetime import datetime

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.load_datetime import load_datetime
from pl_key_value_sqlite_db.save_datetime import save_datetime
from tests.key_types_test import DatetimeKeyForTesting

ARBITRARY_DATETIME_KEY = DatetimeKeyForTesting.DATETIME_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_DATETIME_KEY, "")


def test_save_and_load_datetime() -> None:
    _set_up()
    d = datetime(2000, 1, 1, 1, 1, 1)

    save_datetime(ARBITRARY_DATETIME_KEY, d)
    result = load_datetime(ARBITRARY_DATETIME_KEY)

    assert result == d
