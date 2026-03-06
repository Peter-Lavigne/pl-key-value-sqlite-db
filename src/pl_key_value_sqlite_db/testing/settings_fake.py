from pl_mocks_and_fakes import Fake, stub

from pl_key_value_sqlite_db.settings import Settings, get_settings


class SettingsFake(Fake):
    def __init__(self) -> None:
        self.settings = Settings(
            key_value_db_path="",
        )
        self.settings.key_value_db_path = ""
        stub(get_settings)(self.settings)
