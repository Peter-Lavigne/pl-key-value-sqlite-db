from pl_mocks_and_fakes import mock_for

from pl_key_value_sqlite_db.create_key import create_key
from pl_key_value_sqlite_db.delete_key_value import delete_key_value
from pl_key_value_sqlite_db.delete_key_value_key_unsafe import (
    delete_key_value_key_unsafe,
)
from tests.key_types_test import BoolKeyForTesting

ARBITRARY_KEY = BoolKeyForTesting.BOOL_KEY_FOR_TESTING


def test_delete_key_value() -> None:
    # Arrange: Create a key-value entry
    create_key(ARBITRARY_KEY, "True")

    # Act: Delete the key-value entry
    delete_key_value(ARBITRARY_KEY)

    # Assert: Verify that the delete function was called with the correct key
    mock_for(delete_key_value_key_unsafe).assert_called_once_with(ARBITRARY_KEY.value)
