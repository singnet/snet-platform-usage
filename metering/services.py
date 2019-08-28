import json
import logging

import boto3 as boto3

from settings import CONTRACT_API_ARN, CONTRACT_API_STAGE
from storage import DatabaseStorage
from utils import is_free_call

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
        if is_free_call(usage_details_dict):
            channel_id = usage_details_dict['channel_id']
            group_id = usage_details_dict['group_id']
            user_address = APIUtilityService().get_user_address(group_id, channel_id)
            usage_details_dict['user_address'] = user_address
        self.storage_service.add_usage_data(usage_details_dict)
        return


class APIUtilityService:
    lambda_client = boto3.client('lambda')

    def get_user_address(self, group_id, channel_id):
        lambda_payload = {
            "httpMethod": "GET",
            "requestContext": {"stage": CONTRACT_API_STAGE},
            "path": f"/contract-api/group/{group_id}/channel/{channel_id}"
        }

        try:
            response = self.lambda_client.invoke(
                FunctionName=CONTRACT_API_ARN,
                Payload=json.dumps(lambda_payload)
            )
            response_body_raw = json.loads(
                response.get('Payload').read())['body']
            response_body = json.loads(response_body_raw)
            user_address = response_body['data'][0]['sender']
        except Exception as e:
            print(e)
            raise Exception("Failed to get user address from marketplace")
        return user_address
