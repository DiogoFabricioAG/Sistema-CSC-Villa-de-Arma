from flask_restful import Resource, reqparse
from app.models.socio import Socio
from app.extensions import db
from datetime import datetime
from app.services.google_workspace import obtener_datos
# Actualizamos el parser para incluir los nuevos campos del modelo
parser = reqparse.RequestParser()
parser.add_argument("nombre", type=str, required=True)
parser.add_argument("apellido", type=str, required=True)
parser.add_argument("celular", type=str, required=True)
parser.add_argument("correo_electronico", type=str, required=True)
parser.add_argument("categoria", type=str, required=True)

class SocioResource(Resource):
    def get(self):
        socios = Socio.query.all()
        return [
            {
                "id": s.id,
                "nombre": s.nombre,
                "apellido": s.apellido,
                "celular": s.celular,
                "correo_electronico": s.correo_electronico,
                "categoria": s.categoria,
                "fecha_ingreso": str(s.fecha_ingreso),
            }
            for s in socios
        ]

    def post(self):
        args = parser.parse_args()
        fecha_ingreso = datetime.now().date()

        nuevo = Socio(
            nombre=args["nombre"],
            apellido=args["apellido"],
            celular=args["celular"],
            correo_electronico=args["correo_electronico"],
            categoria=args["categoria"],
            fecha_ingreso=fecha_ingreso,
        )
        db.session.add(nuevo)
        db.session.commit()
        return {"message": "Socio creado", "id": nuevo.id}, 201
    
class OpinionResource(Resource):
    def get(self):
        opinions = obtener_datos(spreadsheet_id='1zHliU1yGnbmIIG0PcJBeKqr0kPH6FbvMaiASBdeuKUI', sheet_name='QuejasOpinionesCSCVilladeArma')
        
        # Format the response as JSON
        response = {
            "status": "success",
            "message": "Opiniones obtenidas con éxito",
            "data": opinions,
            "total": len(opinions) if isinstance(opinions, list) else 0
        }
        
        return response, 200

class SocioGoogleResource(Resource):
    def post(self):
        dataSocios = obtener_datos(spreadsheet_id='1DS-iwBMSHMiJhL-6rKH7UVUMKtNFkGP2ioPFlt7V1yw', sheet_name='Socios CSC Villa de Arma')
        for i in dataSocios:
            if i["Nombre"] == "":
                return {"message": "No se puede crear un socio sin nombre"}, 400

            # Verificar si el socio ya existe en la base de datos
            socio_existente = Socio.query.filter_by(correo_electronico=i["Email"]).first()
            if socio_existente:
                pass
            else:
                nuevo = Socio(
                    nombre=i["Nombre"],
                    apellido=i["Apellido"],
                    celular=i["Numero"],
                    correo_electronico=i["Email"],
                    categoria=i["Categoria"],
                    fecha_ingreso=datetime.strptime(i["Marca temporal"], "%d/%m/%Y %H:%M:%S").date()
                )
                
                db.session.add(nuevo)
        # Commit the session to save the new assembly
        db.session.commit()
        return {"message": "Socios creados"}, 201
    
class SocioDetailResource(Resource):
    def get(self, id):
        socio = Socio.query.get(id)
        if not socio:
            return {"message": "Socio no encontrado"}, 404
        
        return {
            "id": socio.id,
            "nombre": socio.nombre,
            "apellido": socio.apellido,
            "celular": socio.celular,
            "correo_electronico": socio.correo_electronico,
            "categoria": socio.categoria,
            "fecha_ingreso": str(socio.fecha_ingreso),
        }
