from datetime import datetime, timedelta, timezone

from kickbase_api.kickbase import Kickbase
from kickbase_api.exceptions import KickbaseException

from typing import Tuple, Union

from kickbase_api.models.gift import Gift
from kickbase_api.models.league_data import LeagueData
from kickbase_api.models.player import Player
from kickbase_api.models._transforms import parse_date, date_to_string

from .models.user import User

class KickbaseCustom(Kickbase):
    base_url: str = None
    token: str = None
    token_expire: datetime = None
    firebase_token: str = None
    firebase_token_expire: datetime = None
    user: User = None

    _username: str = None
    _password: str = None

    def __init__(self, base_url: str = 'https://api.kickbase.com', firestore_project: str = 'kickbase-bdb0f',
                 google_identity_toolkit_api_key: str = None):
        self.base_url = base_url
        self.firestore_project = firestore_project
        self.google_identity_toolkit_api_key = google_identity_toolkit_api_key

    def login(self, username: str, password: str) -> Tuple[User, LeagueData]:
        data = {
            "email": username,
            "password": password,
            "ext": False
        }

        r = self._do_post("/user/login", data, False)

        if r.status_code == 200:
            j = r.json()
            self.token = j["token"]
            self.token_expire = parse_date(j["tokenExp"])

            self._username = username
            self._password = password

            self.user = User(j["user"])
            league_data = [LeagueData(d) for d in j["leagues"]]
            return j

        elif r.status_code == 401:
            raise KickbaseException()
        else:
            raise KickbaseException()

    def league_user_players(self, league: Union[str, LeagueData], user: Union[str, User], match_day: int = 0) -> Tuple[
        Player]:
        league_id = self._get_league_id(league)
        user_id = self._get_user_id(user)

        r = self._do_get("/leagues/{}/users/{}/players?matchDay={}".format(league_id, user_id, match_day), True)

        if r.status_code == 200:
            return r.json()
        else:
            raise KickbaseException()

    def league_collect_gift(self, league: Union[str, LeagueData]) -> True:
        league_id = self._get_league_id(league)

        r = self._do_post("/leagues/{}/collectgift".format(league_id), {}, True)

        if r.status_code == 200:
            return True
        elif r.status_code == 500:
            return False
        else:
            raise KickbaseException()

    def league_current_gift(self, league: Union[str, LeagueData]) -> True:
        league_id = self._get_league_id(league)

        r = self._do_get("/leagues/{}/currentgift".format(league_id), True)

        if r.status_code == 200:
            return True
            #return Gift(r.json())
        else:
            raise KickbaseException()