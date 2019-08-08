import json

from services import UsageService
from utils import make_response, check_given_key

usage_service = UsageService()


def get_and_validate_requried_params(event):
    try:
        body = json.loads(event['body'])
        if not check_given_key('organization_id', body):
            raise Exception("Org id is compulsory parameter in body request")
    except Exception as e:
        raise e
    return body


def main(event, context):
    usage_detail_dict = get_and_validate_requried_params(event)
    usage_service.save_usage_details(usage_detail_dict)

    response = {
        "statusCode": 201,
        "body": json.dumps({"status": "successfull"})
    }

    return response
