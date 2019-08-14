import logging


def make_response(status_code, body, header=None, ):
    return {
        "statusCode": status_code,
        "headers": header,
        "body": body
    }


def configure_log(logger):
    logger.setLevel(logging.INFO)

    # create a file handler
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    # create a logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)


def validate_request(required_keys, request_body):
    for key in required_keys:
        if key not in request_body:
            return False
    return True


def validator_usage():
    pass
