import logging


def make_response(status_code, body):
    return {
        "statusCode": status_code,
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


def validate_usage_body(request_body):
    required_keys = ["organization_id", "service_id", "username", 'usage_value', 'usage_type',
                     'service_method', 'group_id', 'status', 'start_time', 'end_time']
    for key in required_keys:
        if key not in request_body:
            return False
    return True


def validate_freecalls_request(request):
    required_keys = ['username', 'organization_id', 'service_id']
    for key in required_keys:
        if key not in request:
            return False
    return True


def validator_usage():
    pass
