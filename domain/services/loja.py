from flask import make_response, jsonify, Response
from domain.models import LojaModel
from api.schemas import PlainLojaSchema
from utils import QueryFormatter

from db import db


class LojaService:
    # método responsável por pegar todos as Lojas que estão registradas no banco de dados
    def get_all(self):
        lojas = LojaModel.query.all()

        lojas_formatadas = QueryFormatter().query_list_to_schema_list(lojas, PlainLojaSchema)

        return make_response(jsonify(lojas_formatadas))

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

    # método responsável por atualizar um registro de Loja no banco de dados
    def update(self, loja_data, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        self.update_loja(loja, loja_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def patch(self, loja_data, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        self.update_partially_loja(loja, loja_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def get_by_id(self, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        return make_response(jsonify(
            {
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def delete_by_id(self, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        self.delete_loja(loja)

        return Response(status=204)

    def update_loja(self, dados_loja: LojaModel, dados_loja_nova):
        dados_loja.nome = dados_loja_nova["nome"]

        self.save_loja(dados_loja)

    def update_partially_loja(self, dados_loja: LojaModel, dados_loja_nova):
        dados_loja.nome = dados_loja_nova["nome"]

        self.save_loja(dados_loja)

    @staticmethod
    def save_loja(loja):
        db.session.add(loja)
        db.session.commit()

    @staticmethod
    def delete_loja(loja):
        db.session.delete(loja)
        db.session.commit()
