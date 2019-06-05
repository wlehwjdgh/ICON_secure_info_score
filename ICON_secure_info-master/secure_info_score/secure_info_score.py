from iconservice import *

TAG = 'SecretReadingScore'
TOTAL_SECRET_NUMBER = 3
SECRET_PASSWORD = "1234"

dict_secret = { '1' : "My company did not allow me a Christmas Eve holiday.", '2' : "A is B", '3' : "Maybe A is not B"}
class SecretReadingScore(IconScoreBase):
    
    _DICT_SECRET = 'dict_secret'

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._dict_secret = DictDB(self._DICT_SECRET, db, value_type=str)


    def on_install(self) -> None:
        super().on_install()
        self._dict_secret['1'] = "My company did not allow me a Christmas Eve holiday."
        self._dict_secret['2'] = "A is B"
        self._dict_secret['3'] = "Maybe A is not B"

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def hello(self) -> str:
        Logger.debug(f'Hello, world!', TAG)
        return "Hello123"

    @external(readonly=True)
    def get_secret(self,secretCode: str, secretPassword: str) -> str:
        if secretPassword != SECRET_PASSWORD:
            return "Invalid secret password"
        if int(secretCode) > TOTAL_SECRET_NUMBER:
         return "There is no data corresponding to that secretcode."
        if int(secretCode) == 0:
         return "There is no data corresponding to that secretcode."

        return self._dict_secret[secretCode]

    @external(readonly=True)
    def get_secret_all(self) -> dict:
        return self._dict_secret

    @external(readonly=True)
    def get_secret_1(self) -> str:
        return self._dict_secret['1']

    @external(readonly=True)
    def get_secret_2(self) -> str:
        return self._dict_secret['2']

    @external(readonly=True)
    def get_secret_3(self) -> str:
        return self._dict_secret['3']
