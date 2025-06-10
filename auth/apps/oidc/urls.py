from ninja import NinjaAPI

from .api import router

api = NinjaAPI(title="OIDC Auth Server", version="1.0.0")
api.add_router("/oidc/", router)
