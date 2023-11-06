from flask.views import MethodView
from flask_smorest import Blueprint

from domain.models import LojaModel
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

