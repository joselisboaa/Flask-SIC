from flask.views import MethodView
from flask_smorest import Blueprint

from api.schemas import ClienteSchema, ClientQuerySchemas

blp = Blueprint("Clientes", __name__, "Operações de clientes")

@blp.route('/v1/clientes')
class Clientes(MethodView):

    @blp.arguments(ClientQuerySchemas, location='query')
    @blp.response(200, ClienteSchema(many=True))
    def get(self, *args):
        pass

    @blp.arguments(ClienteSchema)
    @blp.response(201, ClienteSchema)
    def post(self, cliente_data):
        pass


@blp.route('/v1/clientes/<int:cliente_id>')
class Cliente(MethodView):

    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def get(self, cliente_id):
        pass

    @blp.response(204)
    def delete(self, cliente_id):
        pass

    @blp.arguments(ClienteSchema)
    @blp.response(200, ClienteSchema)
    def put(self, cliente_data, cliente_id):
        pass
