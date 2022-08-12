from dependency_injector import containers, providers
from kickbase_api.kickbase import Kickbase

class Container(containers.DeclarativeContainer):
        wiring_config = containers.WiringConfiguration(modules=["flaskr.auth", "flaskr.kickbase"])

        kickbase_service = providers.Singleton(Kickbase)