import json

from services import UsageService
from utils import make_response

usage_service = UsageService()


def get_and_validate_requried_params(event):
    try:
        org_id = event['queryStringParameters']['organization_id']
        service_id = event['queryStringParameters']['service_id']
        user_id = event['queryStringParameters']['user_id']
    except Exception as e:
        raise e

    return org_id, service_id, user_id


def main(event, context):
    org_id, service_id, user_id = get_and_validate_requried_params(event)
    free_call_details = usage_service.get_free_call_details(
        user_id, org_id, service_id)

    return_value = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(free_call_details)
    }

    return return_value
