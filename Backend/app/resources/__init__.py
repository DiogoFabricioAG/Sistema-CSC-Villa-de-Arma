from flask_restful import Api
from app.resources.socio_resource import SocioResource, OpinionResource, SocioGoogleResource
from app.resources.deuda_resource import DeudaResource
from app.resources.asamblea_resource import AsambleaResource

def init_resources(app):
    api = Api(app)
    api.add_resource(SocioResource, "/api/socios")
    api.add_resource(DeudaResource, "/api/deudas")
    api.add_resource(OpinionResource, "/api/opiniones")
    api.add_resource(AsambleaResource, "/api/asambleas")
    api.add_resource(SocioGoogleResource, "/api/socios/google")