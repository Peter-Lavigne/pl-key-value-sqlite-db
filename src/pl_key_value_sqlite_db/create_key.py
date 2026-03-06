from pl_key_value_sqlite_db.create_key_value_key_unsafe import (
    create_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.key_types import BaseKey


def create_key(key: BaseKey, value: str) -> None:
    create_key_value_key_unsafe(key.value, value)
