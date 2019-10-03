import json
import logging

from constants import StatusCode, StatusMessage
from logger import get_logger
from services import UsageService
from utils import (
    validate_request,
    usage_record_add_verify_fields,
    generate_lambda_response,
)

usage_service = UsageService()

logger = get_logger(__name__)

required_keys = [
    "organization_id",
    "service_id",
    "username",
    "usage_value",
    "usage_type",
    "service_method",
    "group_id",
    "status",
    "start_time",
    "end_time",
]


def main(event, context):
    logger.info("Usage record request received")
    try:
        request_dict = json.loads(event["body"])
        if validate_request(required_keys, request_dict):
            usage_detail_dict = usage_record_add_verify_fields(request_dict)
            logging.info(f"usage record after modification: {usage_detail_dict}")
            usage_service.save_usage_details(usage_detail_dict)
            response = "success"
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
