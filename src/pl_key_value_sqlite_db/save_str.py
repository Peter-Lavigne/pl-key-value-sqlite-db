from pl_key_value_sqlite_db.key_types import StrKey
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped


def save_str(key: StrKey, value: str) -> None:
    save_value_untyped(key, value)
