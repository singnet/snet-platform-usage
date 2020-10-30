import json

from constants import StatusCode
from utils import make_response


def main(event, context):
    return make_response(
        status_code=StatusCode.SUCCESS_GET_CODE,
        body=json.dumps({"data": "success"})
    )
