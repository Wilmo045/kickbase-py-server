from flask import (
    Blueprint, request, session
)

from dependency_injector.wiring import Provide, inject
from flask_cors import cross_origin
from kickbasepyserver.classes.kickbase_api.KickbaseCustom import KickbaseCustom
from kickbasepyserver.containers import Container

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.route('/login', methods=['POST'])
@inject
def login(kickbase: KickbaseCustom = Provide[Container.kickbase_service]):
    if request.method == 'POST':
        data = request.get_json()
        session.clear()
        
        j = kickbase.login(data['username'], data['password'])
       # session['user_id'] = user['id']
       # session['kb_league_id'] = leagues[0].id 
        if j is None:
            return 'Incorrect credentials.'
        return j
    return 405

@bp.route('/logout')
def logout():
    session.clear()
    return 200

