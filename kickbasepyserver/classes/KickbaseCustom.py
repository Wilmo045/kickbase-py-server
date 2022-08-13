from kickbase_api.kickbase import Kickbase
from kickbase_api.exceptions import KickbaseException

from typing import Union

from kickbase_api.models.gift import Gift
from kickbase_api.models.league_data import LeagueData

class KickbaseCustom(Kickbase):
    def __init__(self):
        Kickbase.__init__(self)

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