from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
import logging
logger = logging.getLogger("kickbaseCollector")
logger.setLevel(logging.DEBUG)

from kickbase_api.kickbase import Kickbase
from kickbase_api.models.user import User
from kickbase_api.models.league_data import LeagueData
kickbase = Kickbase()
kb_user: User = None
kb_league: LeagueData = None

bp = Blueprint('kickbase', __name__, url_prefix='/kickbase')

@bp.route('/login', methods=('POST',))
def login():
    error = None
    data = request.json
    user, league = kickbase.login(data['username'], data['password'])
    if user is None:
        error = 'Incorrect credentials.'
    if error is None:
        logger.info("Logged in as %s", user.name)
    #return redirect(url_for('kickbase.index'))
    players = kickbase.league_user_players(league[0].id, user)
    return render_template('kickbase/index.html', players=players)

@bp.route('/')
def index():
    #players = kickbase.league_user_players(kb_user, kb_league)
    return render_template('kickbase/index.html', players=players)