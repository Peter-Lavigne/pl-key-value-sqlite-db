from pl_key_value_sqlite_db.delete_key_value_key_unsafe import (
    delete_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.key_types import BaseKey


def delete_key_value(key: BaseKey) -> None:
    delete_key_value_key_unsafe(key.value)
