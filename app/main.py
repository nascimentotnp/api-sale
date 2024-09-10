from flask import Flask
from flask_cors import CORS
from flask_restx import Api

from controllers.products_controller import products_controller, products_ns
from controllers.api_controller import api_controller, api_ns

app = Flask(__name__)
CORS(app, origins="*")

api = Api(app, version='1.0', title='To Order Restaurant',
          description='Documentação API para MVP', doc="/docs")
api.add_namespace(products_ns)
api.add_namespace(api_ns)

app.register_blueprint(products_controller, url_prefix='/products')
app.register_blueprint(api_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
