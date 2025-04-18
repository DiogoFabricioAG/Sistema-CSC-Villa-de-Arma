from app.extensions import db

class Socio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    celular = db.Column(db.String(9), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)  
    fecha_ingreso = db.Column(db.Date)

    def __repr__(self):
        return f"<Socio {self.nombre} {self.apellido}>"