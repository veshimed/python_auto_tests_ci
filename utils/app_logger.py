import os
import time
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'test_results')


def _generate_log_file_name()-> str:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = '{0}/TEST-{1}.txt'.format(RESULTS_DIR, timestr)
    return filename


def get_logger(name: str)-> logging.Logger:
    """Setups logger
    Use in 'application' code:
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    """

    filename = _generate_log_file_name()

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)

    # add file_handler to logger
    logger.addHandler(file_handler)

    # create console handler and set level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # add formatter to console_handler
    console_handler.setFormatter(formatter)

    # add console_handler to logger
    logger.addHandler(console_handler)

    return logger
