from pl_mocks_and_fakes import Fake, mock_for

from pl_key_value_sqlite_db.create_key_value_key_unsafe import (
    create_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.delete_key_value_key_unsafe import (
    delete_key_value_key_unsafe,
)
from pl_key_value_sqlite_db.get_all_key_value_keys import get_all_key_value_keys
from pl_key_value_sqlite_db.load_key_value_unsafe import load_key_value_unsafe
from pl_key_value_sqlite_db.save_key_value_value_unsafe import (
    save_key_value_value_unsafe,
)


class KeyValueSqliteFake(Fake):
    def __init__(self) -> None:
        def _get_all_keys_side_effect() -> list[str]:
            return list(self.store.keys())

        def _create_key_unsafe_side_effect(key: str, value: str) -> None:
            if key not in self.store:
                self.store[key] = value

        def _delete_key_unsafe_side_effect(key: str) -> None:
            del self.store[key]

        def _load_value_unsafe_side_effect(key: str) -> str:
            return self.store[key]

        def _save_value_unsafe_side_effect(key: str, value: str) -> None:
            if key not in self.store:
                msg = f"Key `{key}` does not exist."
                raise Exception(msg)
            self.store[key] = value

        self.store: dict[str, str] = {}

        mock_for(get_all_key_value_keys).side_effect = _get_all_keys_side_effect
        mock_for(
            create_key_value_key_unsafe
        ).side_effect = _create_key_unsafe_side_effect
        mock_for(
            delete_key_value_key_unsafe
        ).side_effect = _delete_key_unsafe_side_effect
        mock_for(load_key_value_unsafe).side_effect = _load_value_unsafe_side_effect
        mock_for(
            save_key_value_value_unsafe
        ).side_effect = _save_value_unsafe_side_effect
