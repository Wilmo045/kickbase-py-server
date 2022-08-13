from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from kickbasepyserver.auth import login_required

from dependency_injector.wiring import Provide, inject

from .classes.KickbaseCustom import KickbaseCustom
from .containers import Container

bp = Blueprint('kickbase', __name__, url_prefix='/kickbase')


@bp.route('/')
@login_required
@inject
def index(kickbase: KickbaseCustom = Provide[Container.kickbase_service]):
    if (kickbase.token is None):
        return redirect(url_for('auth.login'))

    players = kickbase.league_user_players(session.get('kb_league_id'), kickbase.user.id)

    return render_template('kickbase/index.html', players=players)

@bp.route('/gift', methods=('GET', 'POST'))
@login_required
@inject
def gift(kickbase: KickbaseCustom = Provide[Container.kickbase_service]):
    if (kickbase.token is None):
        return redirect(url_for('auth.login'))
    status = 'undefined'
    if request.method == 'POST':
        if kickbase.league_collect_gift :
            status = 'Succesfull Grab'
        status = 'Gift already taken'
    if request.method == 'GET':
        if kickbase.league_current_gift:
            status = 'Gift available'
        status = 'Gift already taken'

    return render_template('kickbase/gift.html', status=status)