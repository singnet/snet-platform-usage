import json
import logging

from constants import StatusCode, StatusMessage, HEADER_POST_RESPONSE
from services import UsageService
from logger import setup_logger
from utils import validate_request, make_response

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)

required_keys = ['username', 'organization_id', 'service_id']


def main(event, context):
    if validate_request(required_keys, event['queryStringParameters']):
        try:
            org_id = event['queryStringParameters']['organization_id']
            service_id = event['queryStringParameters']['service_id']
            username = event['requestContext']['authorizer']['claims']['email']
            free_call_details = usage_service.get_free_call_details(
                username, org_id, service_id)
            return_value = make_response(
                status_code=StatusCode.SUCCESS_GET_CODE,
                header=HEADER_POST_RESPONSE,
                body=json.dumps(free_call_details)
            )

        except Exception as e:
            logger.error(e)
            return_value = make_response(
                status_code=StatusCode.SERVER_ERROR_CODE,
                header=HEADER_POST_RESPONSE,
                body=json.dumps({"error": StatusMessage.SERVER_ERROR_MSG})
            )

    else:
        logger.error('Request validation failed')
        return_value = make_response(
            status_code=StatusCode.BAD_PARAMETERS_CODE,
            header=HEADER_POST_RESPONSE,
            body=json.dumps({"error": StatusMessage.BAD_PARAMETER})
        )

    return return_value
