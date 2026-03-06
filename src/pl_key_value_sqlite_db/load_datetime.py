from datetime import datetime

from pl_key_value_sqlite_db.key_types import DatetimeKey
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped


def load_datetime(key: DatetimeKey) -> datetime:
    return datetime.fromisoformat(load_value_untyped(key))
