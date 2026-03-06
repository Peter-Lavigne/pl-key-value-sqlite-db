from pl_key_value_sqlite_db.key_types import BaseKey
from pl_key_value_sqlite_db.save_key_value_value_unsafe import (
    save_key_value_value_unsafe,
)


def save_value_untyped(key: BaseKey, value: str) -> None:
    save_key_value_value_unsafe(key.value, value)
