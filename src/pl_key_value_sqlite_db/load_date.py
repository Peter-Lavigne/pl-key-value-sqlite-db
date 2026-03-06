from datetime import date

from pl_key_value_sqlite_db.key_types import DateKey
from pl_key_value_sqlite_db.load_value_untyped import load_value_untyped


def load_date(key: DateKey) -> date:
    return date.fromisoformat(load_value_untyped(key))
