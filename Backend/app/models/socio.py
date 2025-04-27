from app.extensions import db
import json
class Socio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(9), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  
    fecha_ingreso = db.Column(db.Date)

    def __repr__(self):
        return json.dumps({
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "celular": self.celular,
            "correo_electronico": self.correo_electronico,
            "categoria": self.categoria,
            "fecha_ingreso": str(self.fecha_ingreso),
        })