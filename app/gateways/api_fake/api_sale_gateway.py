import logging

import requests
import os
from dotenv import load_dotenv

from domain.repository.product_repository import create_products

load_dotenv()

logger = logging.getLogger("json_correlation")
URL_SEND = os.getenv("URL_SALE_API")


def fetch_and_store_products():
    full_url = f"{URL_SEND}/products"
    try:
        response = requests.get(full_url)
        response.raise_for_status()

        products = response.json()

        for product in products:
            new_product = {
                'id': product['id'],
                'title': product['title'],
                'price': product['price'],
                'description': product['description'],
                'category': product['category'],
                'image': product['image'],
                'rating_rate': product['rating']['rate'],
                'rating_count': product['rating']['count']
            }
            #create_products(**new_product)
        return products
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao buscar produtos da API: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Erro de conexão ao tentar acessar a API.")
    except requests.exceptions.Timeout:
        print("A requisição à API demorou muito e atingiu o tempo limite.")
    except requests.exceptions.RequestException as err:
        print(f"Erro ao fazer requisição à API: {err}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
