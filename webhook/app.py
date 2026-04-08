import json
import os

from lithic import Lithic
from lithic.types import CardAuthorizationApprovalRequestWebhookEvent

from authorization import authorize

client = Lithic(
    api_key=os.environ.get("LITHIC_API_KEY", ""),
    webhook_secret=os.environ.get("LITHIC_WEBHOOK_SECRET"),
)


def handler(event, context):
    """
    Responds to incoming ASA requests; returns a constant ack.
    """
    body = event["body"]
    headers = event.get("headers", {})

    if os.environ.get("LITHIC_WEBHOOK_SECRET"):
        asa_request = client.webhooks.parse(payload=body, headers=headers, secret=os.environ.get("LITHIC_WEBHOOK_SECRET"))
    else:
        asa_request = client.webhooks.parse_unsafe(payload=body)
    if not isinstance(asa_request, CardAuthorizationApprovalRequestWebhookEvent):
        print(f"Unexpected event type: {type(asa_request)}")
        return {"statusCode": 400, "body": "Unexpected event type"}

    print(f"Received request: {asa_request.token}")
    authorization_result = authorize(asa_request)
    response_body = {
        "result": authorization_result,
        "token": asa_request.token,
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
