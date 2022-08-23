from flask import (
    Blueprint, jsonify, g, redirect, render_template, request, session, url_for
)

from dependency_injector.wiring import Provide, inject

from ..classes.kickbase_api.KickbaseCustom import KickbaseCustom
from ..containers import Container

bp = Blueprint('gift', __name__, url_prefix='/api/gift')

@bp.route('/gift', methods=('GET', 'POST'))
@inject
def gift(kickbase: KickbaseCustom = Provide[Container.kickbase_service]):
    if (kickbase.token is None):
        return 402
    status = 'undefined'
    if request.method == 'POST':
        if kickbase.league_collect_gift :
            status = 'Succesfull Grab'
        status = 'Gift already taken'
    if request.method == 'GET':
        if kickbase.league_current_gift:
            status = 'Gift available'
        status = 'Gift already taken'

    return status