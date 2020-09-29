import logging
import coloredlogs

def get_logger(name):
    logger = logging.getLogger(name)
    coloredlogs.install(level='DEBUG', logger=logger)
    return logger
