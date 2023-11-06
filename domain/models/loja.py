from db import db


class LojaModel(db.Model):
    __tablename__ = "lojas"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    clientes = db.relationship("ClienteModel", back_populates="loja", lazy="dynamic")
