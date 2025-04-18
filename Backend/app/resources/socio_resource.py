from flask_restful import Resource, reqparse
from app.models.socio import Socio
from app.extensions import db
from datetime import datetime

# Actualizamos el parser para incluir los nuevos campos del modelo
parser = reqparse.RequestParser()
parser.add_argument("nombre", type=str, required=True)
parser.add_argument("apellido", type=str, required=True)
parser.add_argument("celular", type=str, required=True)
parser.add_argument("correo_electronico", type=str, required=True)
parser.add_argument("categoria", type=str, required=True)
parser.add_argument("fecha_ingreso", type=str, required=True)

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
        fecha_ingreso = datetime.strptime(args["fecha_ingreso"], "%d/%m/%Y").date()

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