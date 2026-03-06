from pl_key_value_sqlite_db.key_types import IntKey
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped


def save_int(key: IntKey, value: int) -> None:
    save_value_untyped(key, str(value))
