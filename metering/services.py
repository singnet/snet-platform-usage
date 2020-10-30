import json
import logging
import traceback

import boto3 as boto3

from config import CONTRACT_API_ARN
from config import PAYMENT_MODE_FREECALL_VALUE
from storage import DatabaseStorage

logger = logging.getLogger(__name__)


class UsageService(object):
    storage_service = DatabaseStorage()

    def get_free_call_details(self, username, org_id, service_id, group_id=None):
        total_calls, free_calls = self.storage_service.get_usage_details(
            username, org_id, service_id, group_id)

        if not free_calls:
            free_calls = 0
        if not total_calls:
            total_calls = 0

        response = {"username": username, "org_id": org_id, "service_id": service_id, "total_calls_made": total_calls,
                    "free_calls_allowed": free_calls}

        logger.info(response)
        return response

    def save_usage_details(self, usage_details_dict):
        # nedd to introduce entities when we enhance  feature to this service right now directly using dicts
        if usage_details_dict['payment_mode'] != PAYMENT_MODE_FREECALL_VALUE:
            channel_id = usage_details_dict['channel_id']
            group_id = usage_details_dict['group_id']
            user_address = APIUtilityService().get_user_address(group_id, channel_id)
            usage_details_dict['user_address'] = user_address
        self.storage_service.add_usage_data(usage_details_dict)
        return


class APIUtilityService:

    def __init__(self):
        self.lambda_client = boto3.client('lambda')

    def get_user_address(self, group_id, channel_id):
        lambda_payload = {"pathParameters": {"groupId": group_id, "channelId": channel_id}}
        try:
            response_raw = self.lambda_client.invoke(
                FunctionName=CONTRACT_API_ARN, Payload=json.dumps(lambda_payload))
            response = json.loads(response_raw.get('Payload').read())
            response_body = json.loads(response['body'])
            user_address = response_body['data'][0]['sender']
        except Exception as e:
            traceback.print_exc()
            raise Exception("Failed to get user address from marketplace")
        return user_address
