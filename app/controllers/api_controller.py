from flask import Blueprint
from flask_restx import Namespace, Resource

from gateways.api_fake.api_sale_gateway import fetch_and_store_products

api_ns = Namespace('api', description='Operações relacionadas a API externa')
api_controller = Blueprint('api', __name__)


@api_ns.route('/fetch-external')
class FetchExternalProducts(Resource):
    @api_ns.doc('fetch_external_products')
    def post(self):
        fetch_and_store_products()
        return {'message': 'Produtos da API externa foram salvos com sucesso'}, 201
