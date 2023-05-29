from pathlib import Path
import json

from abc import ABC


class AbsResponseConfig(ABC):

    def __init__(self) -> None:

        base_path = Path(__file__).parent
        print(base_path)
        file_path = (base_path / "../../configs/response_config.json").resolve()
        print(file_path)
        with open(file_path) as json_file:
            user_config_data = json.load(json_file)
        self._user_creds = user_config_data["LOGINS"]
    
    def __repr__(self) -> str:
        return "ResponseConfig()"


class GmailConfig(AbsResponseConfig):
    def __init__(self) -> None:
        super().__init__()
        gcreds = self._user_creds["GMAIL"]
        self.mail_from = gcreds["MAIL_FROM"]
        self.mail_pass = gcreds["MAIL_FROM_OPTIONAL_PASSWD"]
        self.mail_to = gcreds["MAIL_TO"]
