import json

from authorization import authorize


def handler(event, context):
    """
    Responds to incoming ASA requests; returns a constant ack.
    """
    asa_request = json.loads(event["body"])
    print(f"Received request: {asa_request}")
    authorization_result = authorize(asa_request)
    response_body = {
        "result": authorization_result,
        "token": asa_request["token"],
        "avs_result": "MATCH",
        "balance": {"amount": 0, "available": 0},
    }
    print(f"Returning response: {response_body}")
    return {
        "statusCode": 200,
        "headers": {
            "Content-type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        },
        "body": json.dumps(response_body),
    }
