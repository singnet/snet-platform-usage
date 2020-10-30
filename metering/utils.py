import logging


def make_response(status_code, body, header=None):
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


def usage_record_add_verify_fields(usage_detail_dict):
    new_required_keys = {
        'usage_type', 'status', 'usage_value', 'start_time', 'end_time',
        'created_at', 'payment_mode', 'group_id', 'registry_address_key',
        'ethereum_json_rpc_endpoint', 'response_time', 'response_code', 'error_message',
        'version', 'client_type', 'user_details', 'channel_id', 'operation', 'user_address',
        'username', 'org_id', 'service_id', 'resource', 'request_id'
    }
    for key in new_required_keys:
        if (key not in usage_detail_dict) or (usage_detail_dict[key] == ""):
            usage_detail_dict[key] = None
    return usage_detail_dict


def read_from_db(*decorator_args, **decorator_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) == 0:
                raise Exception('should be used in class method')
            func_self = args[0]
            try:
                data = func(*args, **kwargs)
                func_self.session.commit()
                return data
            except:
                func_self.session.rollback()
                raise

        return wrapper

    return decorator
