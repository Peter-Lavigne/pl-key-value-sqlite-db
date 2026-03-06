from datetime import datetime

import pytest
from pl_tiny_clients.current_datetime import current_datetime
from pl_tiny_clients.testing.stubs import stub_current_datetime

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.save_date import save_date
from tests.key_types_test import DateKeyForTesting

ARBITRARY_DATE_KEY = DateKeyForTesting.DATE_KEY_FOR_TESTING


def _set_up() -> None:
    create_key(ARBITRARY_DATE_KEY, "")


def test_save_date_raises_value_error_on_datetime() -> None:
    _set_up()

    with pytest.raises(TypeError):
        save_date(ARBITRARY_DATE_KEY, current_datetime())


def test_save_date_allows_fake_date() -> None:
    _set_up()
    stub_current_datetime(datetime(2000, 1, 1))

    save_date(ARBITRARY_DATE_KEY, current_datetime().date())
