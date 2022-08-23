import functools

from flask import (
    Blueprint, g, redirect, jsonify, request, session, url_for
)

from dependency_injector.wiring import Provide, inject

from kickbasepyserver.classes.kickbase_api.KickbaseCustom import KickbaseCustom
from  kickbasepyserver.classes.kickbase_api.models.user import User
from kickbasepyserver.containers import Container

from kickbasepyserver.db import get_db

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

