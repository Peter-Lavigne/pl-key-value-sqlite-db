from pathlib import Path

from pl_mocks_and_fakes import fake_for, mock_for

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.create_key_value_key_unsafe import (
    create_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import (
    create_key_value_table_if_not_exists,
)
from pl_key_value_sqlite_db.get_all_key_value_keys import get_all_key_value_keys
from pl_key_value_sqlite_db.key_types import BaseKey
from pl_key_value_sqlite_db.key_value_migration import run_migrations
from pl_key_value_sqlite_db.load_str import load_str
from pl_key_value_sqlite_db.testing.settings_fake import SettingsFake
from tests.key_types_test import (
    BoolKeyForTesting,
    DateKeyForTesting,
    DatetimeKeyForTesting,
    IntKeyForTesting,
    StrKeyForTesting,
)

ARBITRARY_KEY = StrKeyForTesting.STR_KEY_FOR_TESTING

TEST_INITIAL_ENTRIES: dict[BaseKey, str] = {
    IntKeyForTesting.INT_KEY_FOR_TESTING: "0",
    DateKeyForTesting.DATE_KEY_FOR_TESTING: "2023-01-01",
    BoolKeyForTesting.BOOL_KEY_FOR_TESTING: "False",
    DatetimeKeyForTesting.DATETIME_KEY_FOR_TESTING: "2023-01-01T00:00:00",
    StrKeyForTesting.STR_KEY_FOR_TESTING: "test",
}


def _set_up(db_path: Path) -> None:
    fake_for(SettingsFake).settings.key_value_db_path = str(db_path)
    db_path.touch()


def test_creates_db_if_not_exists(tmp_path: Path) -> None:
    db_path = tmp_path / "fake_db_path.db"
    _set_up(db_path)
    db_path.unlink()

    run_migrations(TEST_INITIAL_ENTRIES)

    mock_for(create_key_value_table_if_not_exists).assert_called_once()


def test_does_not_create_db_if_exists(tmp_path: Path) -> None:
    # Checking for the file beforehand removes an unnecessary SQL call,
    # which was adding noise to the logs.
    db_path = tmp_path / "fake_db_path.db"
    _set_up(db_path)

    run_migrations(TEST_INITIAL_ENTRIES)

    mock_for(create_key_value_table_if_not_exists).assert_not_called()


def test_create_keys_that_dont_exist_with_initial_values(tmp_path: Path) -> None:
    db_path = tmp_path / "fake_db_path.db"
    _set_up(db_path)

    run_migrations(TEST_INITIAL_ENTRIES)

    assert load_str(ARBITRARY_KEY) == TEST_INITIAL_ENTRIES[ARBITRARY_KEY]


def test_dont_change_keys_that_already_exist(tmp_path: Path) -> None:
    db_path = tmp_path / "fake_db_path.db"
    _set_up(db_path)
    create_key(ARBITRARY_KEY, "test_value")

    run_migrations(TEST_INITIAL_ENTRIES)

    assert load_str(ARBITRARY_KEY) == "test_value"


def test_delete_existing_keys_that_arent_defined(tmp_path: Path) -> None:
    db_path = tmp_path / "fake_db_path.db"
    _set_up(db_path)
    nonexistant_key = "fake_key"
    mock_for(create_key_value_key_unsafe)(nonexistant_key, "test_value")

    run_migrations(TEST_INITIAL_ENTRIES)

    assert nonexistant_key not in mock_for(get_all_key_value_keys)()
