from flask import make_response, jsonify
from domain.models import LojaModel
from api.schemas import PlainLojaSchema

from db import db


class LojaService:
    # método responsável por pegar todos as Lojas que estão registradas no banco de dados
    def get_all(self):
        lojas = LojaModel.query.all()

        return make_response(jsonify(lojas))

    # método responsável por criar um registro de Loja no banco de dados
    def create(self, loja_data):
        loja = LojaModel(**loja_data)

        self.save_loja(loja)

        return make_response(jsonify(
            {
                "message": "Loja criada com sucesso!",
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 201)

    @staticmethod
    def save_loja(loja):
        db.session.add(loja)
        db.session.commit()
