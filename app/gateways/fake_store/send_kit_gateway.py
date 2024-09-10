import logging

import requests
import os
from dotenv import load_dotenv

from config import context

load_dotenv()

logger = logging.getLogger("json_correlation")
URL_SEND_KIT = os.getenv("URL_SEND_KIT")


def full_send_kit(payload: dict):
    full_url = f"{URL_SEND_KIT}/envia-kit-obi/full_send"
    headers = {
        'Content-Type': 'application/json',
        'Origin': context.origin.get()
    }
    try:
        return requests.post(full_url, headers=headers, json=payload)
    except Exception as e:
        logger.error(f"Erro na integração do lote com o OBI. Error -> {e}")
        raise e
