from constants import HEADER_POST_RESPONSE
from constants import StatusCode
from constants import StatusMessage
from logger import get_logger
from services import UsageService

from utils import generate_lambda_response
from utils import validate_request

usage_service = UsageService()

logger = get_logger(__name__)

required_keys = ["organization_id", "service_id"]


def main(event, context):
    logger.info("Free call request received")
    try:
        if validate_request(required_keys, event["queryStringParameters"]):
            org_id = event["queryStringParameters"]["organization_id"]
            service_id = event["queryStringParameters"]["service_id"]
            username = event["queryStringParameters"]["username"]

            logger.info(
                f"Fetched values from request \n"
                f"username: {username} \n"
                f"org_id: {org_id} \n"
                f"service_id: {service_id} \n"
            )

            free_call_details = usage_service.get_free_call_details(
                username, org_id, service_id
            )
            response = free_call_details
            status_code = StatusCode.SUCCESS_GET_CODE
        else:
            logger.error(f"Request validation failed")
            logger.info(event)
            response = StatusMessage.BAD_PARAMETER
            status_code = StatusCode.BAD_PARAMETERS_CODE
    except Exception as e:
        logger.error("Failed to get free call details")
        logger.info(event)
        status_code = (StatusCode.SERVER_ERROR_CODE,)
        response = StatusMessage.SERVER_ERROR_MSG

    return generate_lambda_response(status_code, response)
