from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for
)

from dependency_injector.wiring import Provide, inject

from ..classes.kickbase_api.KickbaseCustom import KickbaseCustom
from ..containers import Container

bp = Blueprint('league', __name__, url_prefix='/api/league')


@bp.route('/<int:leagueId>/userplayers/')
@inject
def userplayers(leagueId, kickbase: KickbaseCustom = Provide[Container.kickbase_service]):
    if (kickbase.token is None):
        return 'Not logged in'

    players = kickbase.league_user_players(str(leagueId), kickbase.user.id)
    players['lineup'] = kickbase.line_up(str(leagueId)).players
    players['lineuptype'] = kickbase.line_up(str(leagueId)).type
   
    return players
