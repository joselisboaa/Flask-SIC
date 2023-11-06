from flask.views import MethodView
from flask_smorest import Blueprint

from domain.services import LojaService
from api.schemas import PlainLojaSchema, LojaQuerySchema

blp = Blueprint("Lojas", __name__, description="Operações de lojas")


@blp.route("/v1/lojas")
class Lojas(MethodView):
    @blp.arguments(LojaQuerySchema, location="query")
    @blp.response(200, PlainLojaSchema)
    def get(self, args):
        return LojaService().get_all()
