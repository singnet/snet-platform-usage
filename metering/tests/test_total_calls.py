import unittest

from models import OrgServiceConfigModel, UsageModel, UserOrgGroupModel
from repository.org_service_config_repository import OrgServiceRepo
from repository.usage_repository import UsageRepository
from repository.user_org_group_repository import UserOrgGroupRepository
from storage import DatabaseStorage


class TestTotalCalls(unittest.TestCase):
    def setUp(self):
        self.org_service_repository = OrgServiceRepo()
        self.usage_repository = UsageRepository()
        self.user_org_group_repository = UserOrgGroupRepository()
        self.storage_service = DatabaseStorage()
        self.org_service_repository.get_default_session().query(
            OrgServiceConfigModel).delete()
        self.org_service_repository.get_default_session().query(UsageModel).delete()
        self.org_service_repository.get_default_session().query(UserOrgGroupModel).delete()
        service_items = list()
        service_items.append(
            OrgServiceConfigModel(
                org_id='snet',
                service_id='example-service',
                free_calls=100,
                effective_end_date='2030-09-12 00:00:00',
                effective_start_date='2011-09-12 00:00:00'
            )
        )
        self.org_service_repository.create_all_items(service_items)

    def test_free_calls(self):
        self.assertEqual((0, 100), self.storage_service.get_usage_details(
            user_name='user@snet', org_id='snet', service_id='example-service'))
        self.org_service_repository.get_default_session().query(UsageModel).delete()

    def test_success_usage_record(self):
        self.storage_service.add_usage_data({
            "type": "response",
            "registry_address_key": "0x5156fde2ca71da4398f8c76763c41bc9633875e4",
            "ethereum_json_rpc_endpoint": "https://ropsten.infura.io",
            "request_id": "bl5tuet35nkvoh9gt9q0",
            "organization_id": "snet",
            "service_id": "example-service",
            "group_id": "3cFvmyLn9UO1jrtuZLerzbgLj6AOtqGo+IBQHtZzV1Q=",
            "service_method": "/example_service.Calculator/add",
            "response_sent_time": "2019-08-08 14:07:15.883501805",
            "request_received_time": "2019-08-08 14:07:15.337318252",
            "response_time": "0.5461",
            "response_code": "Unavailable",
            "error_message": "",
            "version": "v1.0.0",
            'username': 'user@snet',
            "operation": "read",
            "usage_type": "apicall",
            "status": "success",
            "start_time": "2019-08-08 14:07:15.337318252",
            "end_time": "2019-08-08 14:07:15.883501805",
            "usage_value": 1,
            "time_zone": "IST",

        })
        self.storage_service.add_usage_data({
            "type": "response",
            "registry_address_key": "0x5156fde2ca71da4398f8c76763c41bc9633875e4",
            "ethereum_json_rpc_endpoint": "https://ropsten.infura.io",
            "request_id": "bl5tuet35nkvoh9gt9q0",
            "organization_id": "snet",
            "service_id": "example-service",
            "group_id": "3cFvmyLn9UO1jrtuZLerzbgLj6AOtqGo+IBQHtZzV1Q=",
            "service_method": "/example_service.Calculator/add",
            "response_sent_time": "2019-08-08 14:07:15.883501805",
            "request_received_time": "2019-08-08 14:07:15.337318252",
            "response_time": "0.5461",
            "response_code": "Unavailable",
            "error_message": "",
            "version": "v1.0.0",
            'username': 'user@snet',
            "operation": "read",
            "usage_type": "apicall",
            "status": "failed",
            "start_time": "2019-08-08 14:07:15.337318252",
            "end_time": "2019-08-08 14:07:15.883501805",
            "usage_value": 1,
            "time_zone": "IST",

        })
        self.assertEqual((1, 100), self.storage_service.get_usage_details(
            user_name='user@snet', org_id='snet', service_id='example-service'))
        self.org_service_repository.get_default_session().query(UsageModel).delete()

    def tearDown(self):
        self.org_service_repository.get_default_session().query(
            OrgServiceConfigModel).delete()
        self.org_service_repository.get_default_session().query(UsageModel).delete()
        self.org_service_repository.get_default_session().query(UserOrgGroupModel).delete()


if __name__ == '__main__':
    unittest.main()
