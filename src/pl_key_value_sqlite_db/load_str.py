from pl_key_value_sqlite_db.key_types import StrKey
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped


def load_str(key: StrKey) -> str:
    return load_value_untyped(key)
