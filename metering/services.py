import logging

import requests

from settings import MARKETPLACE_CHANNEL_USER_URL
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
            username = APIUtilityService().get_user_name(channel_id, group_id)
            usage_details_dict['username'] = username
        self.storage_service.add_usage_data(usage_details_dict)
        return


class APIUtilityService:

    @staticmethod
    def get_user_name(channel_id, group_id):
        url = MARKETPLACE_CHANNEL_USER_URL.format(group_id, channel_id)
        response = requests.get(url)
        user_data = response.json()
        try:
            username = user_data[0]['username']
        except Exception as e:
            print(e)
            raise Exception("Failed to get username from marketplace")
        return username
