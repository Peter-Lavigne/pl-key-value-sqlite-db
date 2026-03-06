from pl_key_value_sqlite_db.key_types import BoolKey
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped


def load_bool(key: BoolKey) -> bool:
    return load_value_untyped(key) == "True"
