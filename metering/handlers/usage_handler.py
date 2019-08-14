import json
import logging

from logger import setup_logger
from services import UsageService
from utils import validate_usage_body

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)


def main(event, context):
    usage_detail_dict = json.loads(event['body'])

    try:
        if validate_usage_body(usage_detail_dict):
            usage_service.save_usage_details(usage_detail_dict)
            response = {
                "statusCode": 201,
                "body": json.dumps({"status": "successful"})
            }
        else:
            logger.error(f'Request validation failed {usage_detail_dict}')
            response = {
                "statusCode": 400,
                "body": json.dumps({"status": "request validation failed"})
            }
    except Exception as e:
        logger.error(e)
        logger.error(f'failed for request {usage_detail_dict}')
        response = {
            "statusCode": 500,
            "body": json.dumps({"status": "failed"})
        }

    return response
