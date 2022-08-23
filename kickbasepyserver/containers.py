from dependency_injector import containers, providers

from .classes.kickbase_api.KickbaseCustom import KickbaseCustom

class Container(containers.DeclarativeContainer):
        wiring_config = containers.WiringConfiguration(modules=["kickbasepyserver.user.auth", "kickbasepyserver.league.league"])

        kickbase_service = providers.Singleton(KickbaseCustom)