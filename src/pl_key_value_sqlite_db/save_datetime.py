from datetime import datetime

from pl_key_value_sqlite_db.key_types import DatetimeKey
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped


def save_datetime(key: DatetimeKey, value: datetime) -> None:
    save_value_untyped(key, value.isoformat())
