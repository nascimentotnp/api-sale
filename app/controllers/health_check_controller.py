import os
from flask import Flask, jsonify

app = Flask(__name__)

path_base = os.getenv("PATH_BASE", "/sale")
health_path = os.getenv("HEALTH_CHECK", "health")


# Rota de Health Check
@app.route(f'{path_base}/{health_path}', methods=['GET'])
def health_check():
    return jsonify({"message": "OK"}), 200


