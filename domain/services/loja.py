from flask import make_response, jsonify, Response

from domain.models import LojaModel
from api.schemas import PlainLojaSchema

from utils import QueryFormatter, Http
from utils.exceptions import NotFoundException, UniqueException

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

        if self.checar_se_nome_ja_foi_utilizado(loja_data):
            raise UniqueException(
                "O nome da loja deve ser único.",
                "O nome da loja que foi inserido já existe.",
                Http.POST
            )

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

        if loja is None:
            raise NotFoundException(
                "Loja não foi encontrada.",
                "O id da loja inserido não existe no banco de dados.",
                Http.PUT
            )

        if self.checar_se_nome_ja_foi_utilizado(loja_data):
            raise UniqueException(
                "O nome da loja deve ser único.",
                "O nome da loja que foi inserido já existe.",
                Http.PUT
            )

        self.update_loja(loja, loja_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def patch(self, loja_data, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        if loja is None:
            raise NotFoundException(
                "Loja não foi encontrada.",
                "O id da loja inserido não existe no banco de dados",
                Http.PATCH
            )

        if self.checar_se_nome_ja_foi_utilizado(loja_data):
            raise UniqueException(
                "O nome da loja deve ser único.",
                "O nome da loja que foi inserido já existe.",
                Http.PATCH
            )

        self.update_partially_loja(loja, loja_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def get_by_id(self, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        if loja is None:
            raise NotFoundException(
                "Loja não foi encontrada",
                "O id da loja inserido não existe no banco de dados",
                Http.GET
            )

        return make_response(jsonify(
            {
                "loja": PlainLojaSchema().dump(loja)
            }
        ), 200)

    def delete_by_id(self, loja_id):
        loja = LojaModel.query.filter(LojaModel.id == loja_id).first()

        if loja is None:
            raise NotFoundException(
                "Loja não foi encontrada",
                "O id da loja inserido não existe no banco de dados",
                Http.DELETE
            )

        self.delete_loja(loja)

        return Response(status=204)

    def update_loja(self, dados_loja: LojaModel, dados_loja_nova):
        dados_loja.nome = dados_loja_nova["nome"]

        self.save_loja(dados_loja)

    def update_partially_loja(self, dados_loja: LojaModel, dados_loja_nova):
        dados_loja.nome = dados_loja_nova["nome"]

        self.save_loja(dados_loja)

    @staticmethod
    def checar_se_nome_ja_foi_utilizado(loja_data):
        return LojaModel.query.filter(LojaModel.nome == loja_data["nome"]).first() is not None

    @staticmethod
    def save_loja(loja):
        db.session.add(loja)
        db.session.commit()

    @staticmethod
    def delete_loja(loja):
        db.session.delete(loja)
        db.session.commit()
