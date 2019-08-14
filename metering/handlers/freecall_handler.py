import json
import logging

from services import UsageService
from logger import setup_logger
from utils import validate_freecalls_request

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)


def main(event, context):
    if validate_freecalls_request(event['queryStringParameters']):
        try:
            org_id = event['queryStringParameters']['organization_id']
            service_id = event['queryStringParameters']['service_id']
            username = event['queryStringParameters']['username']
            free_call_details = usage_service.get_free_call_details(
                username, org_id, service_id)
            return_value = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body": json.dumps(free_call_details)
            }
        except Exception as e:
            logger.error(e)
            return_value = {
                "statusCode": 500,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                "body": json.dumps({
                    'status': "failed",
                    'error': "Internal server error"
                })
            }
    else:
        logger.error('Request validation failed')
        return_value = {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            },
            "body": json.dumps({
                'status': "failed",
                'error': "Validation failed"
            })
        }
    return return_value
