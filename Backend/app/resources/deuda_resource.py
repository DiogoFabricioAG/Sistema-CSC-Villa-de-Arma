from flask_restful import Resource, reqparse
from app.models.deuda import Deuda, HistorialPago
from app.models.socio import Socio
from app.extensions import db
from datetime import datetime
from app.services.asamblea_services import give_format
parser = reqparse.RequestParser()
parser.add_argument("socio_id", type=int, required=True)
parser.add_argument("monto", type=float, required=True)
parser.add_argument("descripcion", type=str)
parser.add_argument("fecha", type=str, required=True)

class DeudaResource(Resource):
    def get(self):
        deudas = Deuda.query.all()
        socios = {socio.id: socio for socio in Socio.query.all()}
        return [
            {
                "id": d.id,
                "socio": {
                    "id": socio.id,
                    "nombre": socio.nombre,
                    "apellido": socio.apellido,
                    "celular": socio.celular,
                    "correo_electronico": socio.correo_electronico,
                    "categoria": socio.categoria,
                    "fecha_ingreso": str(socio.fecha_ingreso),
                } if (socio := socios.get(d.socio_id)) else None,
                "monto": d.monto,
                "descripcion": d.descripcion,
                "fecha": str(d.fecha),
            }
            for d in deudas
        ]
    
    def post(self):
        args = parser.parse_args()
        args["fecha"] = datetime.strptime(give_format(args["fecha"]), "%d/%m/%Y")
        nueva = Deuda(**args)
        db.session.add(nueva)
        db.session.commit()
        return {"message": "Deuda creada", "id": nueva.id}, 201

class DeudaSocioResource(Resource):
    def get(self, socio_id):
        deudas = Deuda.query.filter_by(socio_id=socio_id).all()
        
        return [
            {
                "id": d.id,
                "monto": d.monto,
                "descripcion": d.descripcion,
                "fecha": str(d.fecha),
            }
            for d in deudas
        ], 200

class HistorialPagoResource(Resource):
    def post(self):
        args = parser.parse_args()
        args["fecha"] = datetime.strptime(give_format(args["fecha"]), "%d/%m/%Y")
        nuevo = HistorialPago(**args)
        db.session.add(nuevo)
        db.session.commit()
        return {"message": "Historial de pago creado", "id": nuevo.id}, 201