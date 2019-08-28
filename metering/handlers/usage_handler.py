import json
import logging

from constants import StatusCode, StatusMessage
from logger import setup_logger
from services import UsageService
from utils import validate_request, make_response

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)

required_keys = ["organization_id", "service_id", "username", 'usage_value', 'usage_type',
                 'service_method', 'group_id', 'status', 'start_time', 'end_time']


def add_verify_fields(usage_detail_dict):
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

    if usage_detail_dict['username'] is not None and usage_detail_dict['user_address'] is None:
        usage_detail_dict['payment_mode'] = 'freecall'
    else:
        usage_detail_dict['payment_mode'] = 'paid'
    return usage_detail_dict


def main(event, context):
    usage_detail_dict = json.loads(event['body'])

    try:
        if validate_request(required_keys, usage_detail_dict):
            usage_detail_dict = add_verify_fields(usage_detail_dict)
            usage_service.save_usage_details(usage_detail_dict)
            response = make_response(
                StatusCode.SUCCESS_GET_CODE,
                json.dumps({"status": StatusMessage.SUCCESS_POST_CODE})
            )
        else:
            logger.error(f'Request validation failed {usage_detail_dict}')
            response = make_response(
                StatusCode.BAD_PARAMETERS_CODE,
                json.dumps({"status": StatusMessage.BAD_PARAMETER})
            )
    except Exception as e:
        logger.error(e)
        logger.error(f'failed for request {usage_detail_dict}')
        response = make_response(
            StatusCode.SERVER_ERROR_CODE,
            json.dumps({"status": StatusMessage.SERVER_ERROR_MSG})
        )

    return response
