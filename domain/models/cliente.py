from db import db


# Classe do modelo da entidade relacional
class ClienteModel(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=False)
    endereco = db.Column(db.String(255), nullable=False, unique=False)

    # Lado muitos (many) guarda a chave estrangeira
    loja_id = db.Column(db.Integer(), db.ForeignKey("lojas.id"), nullable=False)

    # Uma loja tem vários clientes
    loja = db.relationship("LojaModel", back_populates="clientes", uselist=False)
