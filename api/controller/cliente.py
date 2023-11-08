from flask.views import MethodView
from flask_smorest import Blueprint

from api.schemas import ClienteSchema, ClientQuerySchemas
from domain.services import ClienteService

blp = Blueprint("Clientes", __name__, "Operações de clientes")


@blp.route('/v1/clientes')
class Clientes(MethodView):

    @blp.arguments(ClientQuerySchemas)
    @blp.response(200, ClienteSchema(many=True))
    def get(self):
        return ClienteService().get_all()

    @blp.arguments(ClienteSchema)
    @blp.response(201, ClienteSchema)
    def post(self, cliente_data):
        return ClienteService().create(cliente_data)


@blp.route('/v1/clientes/<int:cliente_id>')
class Cliente(MethodView):

    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def get(self, cliente_id):
        return ClienteService().get_by_id(cliente_id)

    @blp.response(204)
    def delete(self, cliente_id):
        return ClienteService().delete_by_id(cliente_id)

    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def patch(self, cliente_data, cliente_id):
        return ClienteService().patch(cliente_data, cliente_id)

    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def put(self, cliente_data, cliente_id):
        return ClienteService().update(cliente_data, cliente_id)
