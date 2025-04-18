from flask_restful import Resource, reqparse
from app.models.deuda import Deuda
from app.extensions import db

parser = reqparse.RequestParser()
parser.add_argument("socio_id", type=int, required=True)
parser.add_argument("monto", type=float, required=True)
parser.add_argument("descripcion", type=str)
parser.add_argument("fecha", type=str, required=True)

class DeudaResource(Resource):
    def get(self):
        deudas = Deuda.query.all()
        return [
            {
                "id": d.id,
                "socio_id": d.socio_id,
                "monto": d.monto,
                "descripcion": d.descripcion,
                "fecha": str(d.fecha),
            }
            for d in deudas
        ]

    def post(self):
        args = parser.parse_args()
        nueva = Deuda(**args)
        db.session.add(nueva)
        db.session.commit()
        return {"message": "Deuda creada", "id": nueva.id}, 201
