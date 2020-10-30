import json
import logging

from constants import StatusCode, StatusMessage
from logger import setup_logger
from services import UsageService
from utils import validate_request, make_response, usage_record_add_verify_fields

usage_service = UsageService()

setup_logger()
logger = logging.getLogger(__name__)

required_keys = ["organization_id", "service_id", "username", 'usage_value', 'usage_type',
                 'service_method', 'group_id', 'status', 'start_time', 'end_time']


def main(event, context):
    request_dict = json.loads(event['body'])

    try:
        if validate_request(required_keys, request_dict):
            usage_detail_dict = usage_record_add_verify_fields(request_dict)
            print(f"usage record after modification: {usage_detail_dict}")
            usage_service.save_usage_details(usage_detail_dict)
            response = make_response(
                StatusCode.SUCCESS_GET_CODE,
                json.dumps({"status": StatusMessage.SUCCESS_POST_CODE})
            )
        else:
            logger.error(f'Request validation failed {request_dict}')
            response = make_response(
                StatusCode.BAD_PARAMETERS_CODE,
                json.dumps({"status": StatusMessage.BAD_PARAMETER})
            )
    except Exception as e:
        logger.error(e)
        logger.error(f'failed for request {request_dict}')
        response = make_response(
            StatusCode.SERVER_ERROR_CODE,
            json.dumps({"status": StatusMessage.SERVER_ERROR_MSG})
        )

    return response


if __name__ == '__main__':
    event = {
        "body": json.dumps(
            {'type': 'response', 'registry_address_key': '0xdce9c76ccb881af94f7fb4fac94e4acc584fa9a5',
             'ethereum_json_rpc_endpoint': 'https://mainnet.infura.io/v3/09027f4a13e841d48dbfefc67e7685d5',
             'request_id': 'budno82mjn88juddh8tg', 'organization_id': 'snet', 'service_id': 'example-service',
             'group_id': 'EoFmN3nvaXpf6ew8jJbIPVghE5NXfYupFF7PkRmVyGQ=',
             'service_method': '/example_service.Calculator/add', 'response_sent_time': '2020-10-30 02:36:16.516130074',
             'request_received_time': '2020-10-30 02:36:16.169759062', 'response_time': '0.3464', 'response_code': 'OK',
             'error_message': None, 'version': 'v4.0.0', 'client_type': None, 'user_details': None,
             'user_agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
             'channel_id': '5', 'username': None, 'operation': 'read', 'usage_type': 'apicall', 'status': 'success',
             'start_time': '2020-10-30 02:36:16.169759062', 'end_time': '2020-10-30 02:36:16.516130074',
             'usage_value': 1, 'time_zone': '', 'payment_mode': 'fr', 'user_address': None, 'resource': None,
             'org_id': None, 'created_at': None}
        )
    }
    main(event, None)
