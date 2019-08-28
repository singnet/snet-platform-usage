import logging.config


def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


if __name__ == '__main__':
    setup_logger()
    logger = logging.getLogger()
    logger.info("hi, it is test")
