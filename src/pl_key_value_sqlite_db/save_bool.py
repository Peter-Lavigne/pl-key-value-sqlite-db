from pl_key_value_sqlite_db.key_types import BoolKey
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped


def save_bool(key: BoolKey, value: bool) -> None:
    save_value_untyped(key, str(value))
