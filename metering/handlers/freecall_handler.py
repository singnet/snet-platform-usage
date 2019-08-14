import json
import logging

from constants import StatusCode, StatusMessage
from services import UsageService
from logger import setup_logger
from utils import validate_request, make_freecalls_response

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)

required_keys = ['username', 'organization_id', 'service_id']


def main(event, context):
    if validate_request(event['queryStringParameters']):
        try:
            org_id = event['queryStringParameters']['organization_id']
            service_id = event['queryStringParameters']['service_id']
            username = event['queryStringParameters']['username']
            free_call_details = usage_service.get_free_call_details(
                username, org_id, service_id)
            return_value = make_freecalls_response(
                StatusCode.SUCCESS_GET_CODE,
                json.dumps(free_call_details)
            )

        except Exception as e:
            logger.error(e)
            return_value = make_freecalls_response(
                StatusCode.SERVER_ERROR_CODE,
                json.dumps({"error": StatusMessage.SERVER_ERROR_MSG})
            )

    else:
        logger.error('Request validation failed')
        return_value = make_freecalls_response(
            StatusCode.BAD_PARAMETERS_CODE,
            json.dumps({"error": StatusMessage.BAD_PARAMETER})
        )

    return return_value
