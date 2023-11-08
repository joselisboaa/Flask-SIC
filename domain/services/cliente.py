from flask import make_response, jsonify, Response

from domain.models import ClienteModel, LojaModel
from api.schemas import ClienteSchema, PlainClienteSchema
from utils import QueryFormatter, NotFoundException, Http, DependencyEntityNotExist

from db import db


class ClienteService:
    # método responsável por pegar todos os Clientes que estão registradas no banco de dados
    def get_all(self):
        clientes = ClienteModel.query.all()

        clientes_formatados = QueryFormatter().query_list_to_schema_list(clientes, PlainClienteSchema)

        return make_response(jsonify(clientes_formatados))

    # método responsável por criar um registro de Cliente no banco de dados
    def create(self, cliente_data):
        cliente = ClienteModel(**cliente_data)

        if self.checar_se_a_loja_existe(cliente_data):
            raise DependencyEntityNotExist(
                "Loja não encontrada.",
                "A loja associada a esse cliente não existe.",
                Http.POST
            )

        self.save_cliente(cliente)

        return make_response(jsonify(
            {
                "message": "Loja criada com sucesso!",
                "cliente": ClienteSchema().dump(cliente)
            }
        ), 201)

    # método responsável por atualizar um registro de Cliente no banco de dados,
    # podendo atualizar totalmente o registro
    def update(self, cliente_data, cliente_id):
        cliente = ClienteModel.query.filter(ClienteModel.id == cliente_id).first()

        if cliente is None:
            raise NotFoundException(
                "Cliente não foi encontrado",
                "O id do cliente inserido não existe no banco de dados.",
                Http.PUT
            )

        if self.checar_se_a_loja_existe(cliente_data):
            raise DependencyEntityNotExist(
                "Loja não encontrada.",
                "A loja associada a esse cliente não existe.",
                Http.POST
            )

        self.update_loja(cliente, cliente_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "cliente": ClienteSchema().dump(cliente)
            }
        ), 200)

    # método responsável por atualizar um registro de Cliente no banco de dados,
    # podendo somente atualizar parcialmente.
    def patch(self, cliente_data, cliente_id):
        cliente = ClienteModel.query.filter(ClienteModel.id == cliente_id).first()

        if cliente is None:
            raise NotFoundException(
                "Cliente não foi encontrado",
                "O id do cliente inserido não existe no banco de dados.",
                Http.PATCH
            )

        self.update_partially_cliente(cliente, cliente_data)

        return make_response(jsonify(
            {
                "message": "Loja atualizada com sucesso!",
                "cliente": ClienteSchema().dump(cliente)
            }
        ), 200)

    def get_by_id(self, cliente_id):
        cliente = ClienteModel.query.filter(ClienteModel.id == cliente_id).first()

        if cliente is None:
            raise NotFoundException(
                "Cliente não foi encontrado",
                "O id do cliente inserido não existe no banco de dados",
                Http.GET
            )

        return make_response(jsonify(
            {
                "cliente": ClienteSchema().dump(cliente)
            }
        ), 200)

    def delete_by_id(self, cliente_id):
        cliente = ClienteModel.query.filter(ClienteModel.id == cliente_id).first()

        if cliente is None:
            raise NotFoundException(
                "Loja não foi encontrada",
                "O id da loja inserido não existe no banco de dados",
                Http.DELETE
            )

        self.delete_cliente(cliente)

        return Response(status=204)

    def update_loja(self, dados_cliente: ClienteModel, dados_novo_cliente):
        dados_cliente.nome = dados_novo_cliente["nome"]
        dados_cliente.endereco = dados_novo_cliente["endereco"]
        dados_cliente.loja_id = dados_novo_cliente["loja_id"]

        self.save_cliente(dados_cliente)

    def update_partially_cliente(self, dados_cliente: ClienteModel, dados_novo_cliente):
        dados_cliente.nome = dados_novo_cliente["nome"]

        self.save_cliente(dados_cliente)

    @staticmethod
    def checar_se_a_loja_existe(cliente_data):
        return LojaModel.query.filter(LojaModel.id == cliente_data["loja_id"]) is not None

    @staticmethod
    def save_cliente(cliente):
        db.session.add(cliente)
        db.session.commit()

    @staticmethod
    def delete_cliente(cliente):
        db.session.delete(cliente)
        db.session.commit()
