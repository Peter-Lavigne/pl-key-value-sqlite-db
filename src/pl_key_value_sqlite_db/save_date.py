from datetime import date

from pl_key_value_sqlite_db.key_types import DateKey
from pl_key_value_sqlite_db.save_value_untyped import save_value_untyped


def save_date(key: DateKey, value: date) -> None:
    if value.__class__.__name__ != "date":
        msg = f"Expected date object, got {value.__class__.__name__}"
        raise TypeError(msg)
    save_value_untyped(key, value.isoformat())
