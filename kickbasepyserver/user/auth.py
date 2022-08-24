from flask import (
    Blueprint, request, session, make_response, jsonify
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
        username = request.form.get('username')
        password = request.form.get('password')
        session.clear()
        r = kickbase.login(username, password)
        if r.status_code == 200:
            #change response to hide token etc.
            return r.json()
        return make_response(jsonify(success='Login failed'))

@bp.route('/logout')
def logout():
    session.clear()
    return 200

