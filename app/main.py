import os
from flask import Flask, jsonify
from flask.cli import load_dotenv
import logging
from flask_cors import CORS
from flask_restx import Api

from controllers import health_check_controller
from controllers.health_check_controller import health_ns
from controllers.products_controller import products_controller, products_ns
from controllers.api_controller import api_controller, api_ns
from config.log import setup_log
from config.timezone import set_default_timezone
from gateways.api_fake.api_sale_gateway import fetch_and_store_products
from domain.repository.product_repository import initialize_products_if_empty
from gateways.databases.connection import engine

load_dotenv()
set_default_timezone()
setup_log()

app = Flask(__name__)
CORS(app, origins="*")

api = Api(app, version='1.0', title='Seller', description='Documentação API para MVP', doc="/docs")

api.add_namespace(products_ns)
api.add_namespace(api_ns, path='/api')
api.add_namespace(health_ns)

app.register_blueprint(products_controller, url_prefix='/products')
app.register_blueprint(api_controller, url_prefix='/api')


# app.register_blueprint(health_check_controller, url_prefix='/health')

def init_database():
    from gateways.databases.gateway_database import Base
    Base.metadata.create_all(engine)

    products = fetch_and_store_products()
    if products:
        initialize_products_if_empty(products)


if __name__ == '__main__':
    init_database()

    app.run(host='localhost', port=int(os.getenv("PORT", 8080)), debug=os.getenv("DEBUG", "False") == "True")
