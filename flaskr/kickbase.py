from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.auth import login_required

from kickbase_api.kickbase import Kickbase

from dependency_injector.wiring import Provide, inject
from .containers import Container

bp = Blueprint('kickbase', __name__, url_prefix='/kickbase')


@bp.route('/')
@inject
def index(kickbase: Kickbase = Provide[Container.kickbase_service]):
    
    players = kickbase.league_user_players(session.get('kb_league_id'), kickbase.user.id)

    return render_template('kickbase/index.html', players=players)