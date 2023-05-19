from utils.db import db


class Predio(db.Model):
    idPredio = db.Column(db.Integer, primary_key=True)
    nombrePropietario = db.Column(db.String(100))
    direccionPredio = db.Column(db.String(100))
    areaPredio = db.Column(db.Float)
    tipoSuelo = db.Column(db.String(100))
    valorPredio = db.Column(db.Float)
    distrito = db.Column(db.String(100))

    def __init__(self, nombrePropietario, direccionPredio, areaPredio, tipoSuelo, valorPredio, distrito):       
        self.nombrePropietario = nombrePropietario
        self.direccionPredio = direccionPredio
        self.areaPredio = areaPredio
        self.tipoSuelo = tipoSuelo
        self.valorPredio = valorPredio
        self.distrito = distrito
        
