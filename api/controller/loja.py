from flask.views import MethodView
from flask_smorest import Blueprint

from domain.services import LojaService
from api.schemas import PlainLojaSchema, LojaQuerySchema

blp = Blueprint("Lojas", __name__, description="Operações de lojas")


@blp.route("/v1/lojas")
class Lojas(MethodView):
    @blp.arguments(LojaQuerySchema, location="query")
    @blp.response(200, PlainLojaSchema(many=True))
    def get(self, args):
        return LojaService().get_all()

    @blp.arguments(PlainLojaSchema)
    @blp.response(201, PlainLojaSchema)
    def post(self, loja_data):
        return LojaService().create(loja_data)


@blp.route("/v1/lojas/<int:loja_id>")
class Loja(MethodView):
    @blp.arguments(PlainLojaSchema)
    @blp.response(200, PlainLojaSchema)
    def put(self, loja_data, loja_id):
        return LojaService().update(loja_data, loja_id)

    @blp.arguments(PlainLojaSchema)
    @blp.response(200, PlainLojaSchema)
    def patch(self, loja_data, loja_id):
        return LojaService().patch(loja_data, loja_id)

    @blp.response(200, PlainLojaSchema)
    def get_by_id(self, loja_id):
        return LojaService().get_by_id(loja_id)

    @blp.response(204)
    def delete(self, loja_id):
        return LojaService().delete_by_id(loja_id)
