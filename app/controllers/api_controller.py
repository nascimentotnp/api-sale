import logging

from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource

from gateways.api_fake.api_sale_gateway import fetch_and_store_products

api_ns = Namespace('api', description='Operações relacionadas a API externa')
api_controller = Blueprint('api', __name__)


@api_ns.route('/fetch-products')
class FetchExternalProducts(Resource):
    def get(self):
        try:
            return fetch_and_store_products()
        except Exception as e:
            return {"error": str(e)}, 500
