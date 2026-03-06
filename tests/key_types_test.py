from pl_key_value_sqlite_db.key_types import (
    BoolKey,
    DateKey,
    DatetimeKey,
    IntKey,
    StrKey,
)


class IntKeyForTesting(IntKey):
    INT_KEY_FOR_TESTING = "int_key_for_testing"


class DateKeyForTesting(DateKey):
    DATE_KEY_FOR_TESTING = "date_key_for_testing"


class BoolKeyForTesting(BoolKey):
    BOOL_KEY_FOR_TESTING = "bool_key_for_testing"


class DatetimeKeyForTesting(DatetimeKey):
    DATETIME_KEY_FOR_TESTING = "datetime_key_for_testing"


class StrKeyForTesting(StrKey):
    STR_KEY_FOR_TESTING = "str_key_for_testing"
