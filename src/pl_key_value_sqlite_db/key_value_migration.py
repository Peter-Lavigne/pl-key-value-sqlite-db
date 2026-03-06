import logging
from pathlib import Path

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.create_key_value_table_if_not_exists import (
    create_key_value_table_if_not_exists,
)
from pl_key_value_sqlite_db.delete_key_value_key_unsafe import (
    delete_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.get_all_key_value_keys import get_all_key_value_keys
from pl_key_value_sqlite_db.key_types import BaseKey
from pl_key_value_sqlite_db.settings import get_settings


def run_migrations(initial_entries: dict[BaseKey, str]) -> None:
    logging.info("Checking for migrations to run.")

    if not Path(get_settings().key_value_db_path).exists():
        create_key_value_table_if_not_exists()

    existing_keys = get_all_key_value_keys()

    for key, value in initial_entries.items():
        if key.value not in existing_keys:
            create_key(key, value)

    for key in existing_keys:
        if key not in [k.value for k in initial_entries]:
            delete_key_value_key_unsafe(key)

    logging.info("Finished running migrations.")
