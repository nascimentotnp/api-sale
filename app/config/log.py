import logging
from datetime import datetime
from logging import config

import asgi_correlation_id
from pythonjsonlogger import jsonlogger

from config import context

json_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "request_id_filter": {
            "()": "config.log.RequestIdLogFilter"
        }
    },
    "formatters": {
        "json_correlation": {
            "format": "%(asctime)s %(levelname)s [%(origin)s] [%(document_type)s] [%(correlation_id)s] "
                      "[%(document_correlation_id)s] [%(integration_batch_id)s] [%(branch_code)s]"
                      " %(threadName)s %(filename)s %(funcName)s %(lineno)s %(message)s ",
            "class": "config.log.CustomJsonFormatter"
        }
    },
    "handlers": {
        "json_correlation": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "json_correlation",
            "stream": "ext://sys.stdout",
            "filters": ["request_id_filter"]
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json_correlation"]
        }
    }
}


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def process_log_record(self, log_record):
        log_record['asctime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        return super(CustomJsonFormatter, self).process_log_record(log_record)


class RequestIdLogFilter(logging.Filter):
    def filter(self, record):
        record.correlation_id = asgi_correlation_id.correlation_id.get()
        record.origin = context.origin.get()
        record.document_correlation_id = context.document_correlation_id.get()
        record.integration_batch_id = context.integration_batch_id.get()
        record.branch_code = context.branch_code.get()
        record.document_type = context.document_type.get()
        return True


def setup_log():
    logging.config.dictConfig(json_config)

