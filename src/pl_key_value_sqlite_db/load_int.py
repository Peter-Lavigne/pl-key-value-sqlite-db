from pl_key_value_sqlite_db.key_types import IntKey
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped


def load_int(key: IntKey) -> int:
    return int(load_value_untyped(key))
