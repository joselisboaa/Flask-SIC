from db import db
from domain.models import LojaModel


class LojaService:

    def get_all(self):

        return LojaModel.query.all()
