from app.extensions import db
from datetime import datetime

class Deuda(db.Model):
    __tablename__ = 'deudas'

    id = db.Column(db.Integer, primary_key=True)
    socio_id = db.Column(db.Integer, db.ForeignKey('socio.id'), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    # Relación con la tabla Socio
    socio = db.relationship('Socio', backref=db.backref('deudas', lazy=True))

    def __init__(self, socio_id, monto, descripcion, fecha):
        self.socio_id = socio_id
        self.monto = monto
        self.descripcion = descripcion
        self.fecha = fecha

class HistorialPago(db.Model):
    __tablename__ = 'historial_pagos'

    id = db.Column(db.Integer, primary_key=True)
    deuda_id = db.Column(db.Integer, db.ForeignKey('deudas.id'), nullable=False)
    monto_pagado = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    # Relación con la tabla Deuda
    deuda = db.relationship('Deuda', backref=db.backref('historial_pagos', lazy=True))

    def __init__(self, deuda_id, monto_pagado, fecha_pago):
        self.deuda_id = deuda_id
        self.monto_pagado = monto_pagado
        self.fecha_pago = fecha_pago