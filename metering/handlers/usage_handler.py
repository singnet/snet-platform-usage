import json
import logging

from constants import StatusCode, StatusMessage
from logger import setup_logger
from services import UsageService
from utils import validate_request, make_response, usage_record_add_verify_fields

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)

required_keys = ["organization_id", "service_id", "username", 'usage_value', 'usage_type',
                 'service_method', 'group_id', 'status', 'start_time', 'end_time']


def main(event, context):
    request_dict = json.loads(event['body'])

    try:
        if validate_request(required_keys, request_dict):
            print(f"usage record before modification: {request_dict}")
            usage_detail_dict = usage_record_add_verify_fields(request_dict)
            print(f"usage record after modification: {usage_detail_dict}")
            usage_service.save_usage_details(usage_detail_dict)
            response = make_response(
                StatusCode.SUCCESS_GET_CODE,
                json.dumps({"status": StatusMessage.SUCCESS_POST_CODE})
            )
        else:
            logger.error(f'Request validation failed {request_dict}')
            response = make_response(
                StatusCode.BAD_PARAMETERS_CODE,
                json.dumps({"status": StatusMessage.BAD_PARAMETER})
            )
    except Exception as e:
        logger.error(e)
        logger.error(f'failed for request {request_dict}')
        response = make_response(
            StatusCode.SERVER_ERROR_CODE,
            json.dumps({"status": StatusMessage.SERVER_ERROR_MSG})
        )

    return response

