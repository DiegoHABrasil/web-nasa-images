import logging
import logging.config
from structlog import getLogger


class AppLogger(object):
    "Logging class used by application"


    def __init__(self, log_name="web-nasa-images"):

        self.log_name = log_name

        logging.config.dictConfig({
            'version': 1,
            'formatters': {'text': {
                'format': '%(funcName)s %(module)s %(lineno)d %(message)s',
            }},
            'handlers': {'console': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter': 'text'
            }},
            'root': {
                'level': 'INFO',
                'handlers': ['console']
            }
        })

        self.logger = getLogger('web-nasa-images')


    def get_logger(self):
        
        return self.logger

        