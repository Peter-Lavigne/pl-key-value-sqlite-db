from pl_key_value_sqlite_db.key_types import BaseKey
from pl_key_value_sqlite_db.load_key_value_unsafe import load_key_value_unsafe


def load_value_untyped(key: BaseKey) -> str:
    return load_key_value_unsafe(key.value)
