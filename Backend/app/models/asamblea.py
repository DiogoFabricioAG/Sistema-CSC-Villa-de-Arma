from app.extensions import db

class Asamblea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_asamblea = db.Column(db.Date)
    asistentes_asamblea = db.Column(db.String(50), nullable=False)
    acta_asamblea = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Asamblea {self.fecha_asamblea}>"