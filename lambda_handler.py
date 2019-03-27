import json
import os

from auth_token import Token
from constant import DEFAULT_NETWORK_ID

def request_handler(event, context):
    print(event)
    if 'path' not in event:
        return get_response("400", {"status": "failed", "error": "Bad Request"})
    try:
        path = event['path'].lower()
        data = None
        if "/register" == path:
            payload = event['body']
            payload_dict = payload_check(payload=payload, path=path)
            net_id = DEFAULT_NETWORK_ID
            token_instance = Token(net_id)
            data = token_instance.process_token(daemon_id=payload_dict['daemonId'])
            if data is None:
                response = get_response("400", {"status": "failed", "error": "Bad Request"})
            else:
                if data.get('error', '') == '':
                    print(data)
                    response = get_response("200", {"status": "success", "data": data})
                else:
                    error = data['error']
                    data.pop('error')
                    response = get_response("200", {"status": "failed", "data": data, "error": error})
        elif "/event" == path:
            try:
                payload_dict = event['headers']
                print("Processing [" + str(path) + "] with body [" + str(payload_dict) + "]")
                net_id = 42
                token_instance = Token(net_id)
                data = token_instance.validate_token(daemon_id=payload_dict['x-daemonid'], token=payload_dict['x-token'])
                response = get_lambda_authorizer_response_format(event=event, allow=data['validated'])
            except Exception as e:
                print(repr(e))
                response = get_lambda_authorizer_response_format(event=event, allow=False)

    except Exception as e:
        response = get_response(500, {"status": "failed",
                                      "error": repr(e)})

    return response


def payload_check(payload, path):
    payload_dict = None
    if payload is not None and len(payload) > 0:
        payload_dict = json.loads(payload)
    print("Processing [" + str(path) + "] with body [" + str(payload) + "]")
    return payload_dict


# Generate response JSON that API gateway expects from the lambda function
def get_response(status_code, message):
    return {
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            "X-Requested-With": '*',
            "Access-Control-Allow-Headers": 'Access-Control-Allow-Origin, Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with',
            "Access-Control-Allow-Origin": '*',
            "Access-Control-Allow-Methods": 'GET,OPTIONS,POST'
        }
    }


def get_lambda_authorizer_response_format(event, allow):
    print(allow)
    response = {
        "principalId": os.environ['principalId'],
        "policyDocument": {
            "Version": '2012-10-17',
            "Statement": [
                {
                    "Action": 'execute-api:Invoke',
                    "Resource": event['methodArn']
                }
            ]
        }
    }
    if allow:
        response["policyDocument"]["Statement"][0]["Effect"] = 'Allow'
    else:
        response["policyDocument"]["Statement"][0]["Effect"] = 'Deny'

    print(response)
    return response
