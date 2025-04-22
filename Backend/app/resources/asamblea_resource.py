from flask_restful import Resource, reqparse
from app.models.asamblea import Asamblea
from app.extensions import db
from app.services.asamblea_services import obtener_asambleas,get_image_id,give_format
from app.services.google_workspace import obtener_datos
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument("fecha_asamblea", type=str, required=True)
parser.add_argument("asistentes_asamblea", type=str, required=True)
parser.add_argument("acta_asamblea", type=str, required=True)

class AsambleaResource(Resource):
    def get(self):
        asambleas = Asamblea.query.all()
        return [
            {
                "id": a.id,
                "fecha_asamblea": str(a.fecha_asamblea),
                "asistentes_asamblea": a.asistentes_asamblea,
                "acta_asamblea": a.acta_asamblea,
            }
            for a in asambleas
        ]

    def post(self):
        asambleas_existentes = obtener_datos(
            spreadsheet_id='1VKPnJ7fapW2FFVe4rHaoB26HOgzJhDsAgqLNNLcrrGo',
            sheet_name='Cargar Asambleas (respuestas)'
        )
        for i in asambleas_existentes:
            if i["Fecha Asamblea"] == "":
                return {"message": "No se puede crear una asamblea sin fecha"}, 400

            # Verificar si la asamblea ya existe en la base de datos
            datetime_valid = datetime.strptime(i["Fecha Asamblea"], "%d/%m/%Y")

            asamblea_existente = Asamblea.query.all()
            lista_fechas = list(map(lambda x: give_format(str(x.fecha_asamblea)), asamblea_existente))

            if i["Fecha Asamblea"] in lista_fechas:
                pass
            else:
                nueva = Asamblea(
                    fecha_asamblea=datetime_valid,
                    asistentes_asamblea=get_image_id(i["Imagen de Asistentes"]),
                    acta_asamblea=get_image_id(i["Imagen de Acta de Reunión"])
                )
            
                db.session.add(nueva)
            # Commit the session to save the new assembly
        try:
            db.session.commit()
            return {"message": "Asambleas creadas", "id": nueva.id}, 201

        except Exception as e:
            db.session.rollback()
            return {"message": "Error al crear la asamblea", "error": str(e)}, 500
        finally:
            db.session.close()

    