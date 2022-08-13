from dependency_injector import containers, providers

from .lib.KickbaseCustom import KickbaseCustom

class Container(containers.DeclarativeContainer):
        wiring_config = containers.WiringConfiguration(modules=["kickbasepyserver.auth", "kickbasepyserver.kickbase"])

        kickbase_service = providers.Singleton(KickbaseCustom)