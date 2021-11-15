import argparse
import json

import requests

from util import read_api_key

VALID_ACTIONS = [
    "authorize",
    "clearing",
    "return",
    "void",
]


def _construct_clearing_void_call(args):
    if not args.token:
        raise ValueError(
            "A transaction token is required when simulating a clearance or a void"
        )

    request_body = {
        "token": args.token,
    }

    if args.amount is not None:
        request_body["amount"] = args.amount

    return request_body


def _construct_authorize_return_call(args):
    if not args.pan:
        raise ValueError(
            "A PAN is required when simulating an authorization or a return"
        )

    return {
        "descriptor": args.descriptor,
        "amount": args.amount,
        "pan": args.pan,
    }


def simulate(api_key: str, action: str, request_body: dict):
    resp = requests.post(
        f"https://sandbox.lithic.com/v1/simulate/{action}",
        headers={
            "Authorization": f"api-key {api_key}",
            "Content-type": "application/json",
        },
        json=request_body,
    )
    resp.raise_for_status()
    print(json.dumps(resp.json()))


if __name__ == "__main__":
    api_key = read_api_key()

    parser = argparse.ArgumentParser()

    parser.add_argument("action", type=str, choices=VALID_ACTIONS)
    parser.add_argument("--token", type=str)
    parser.add_argument("--amount", type=int, default=0)
    parser.add_argument("--descriptor", type=str, default="Sample descriptor")
    parser.add_argument("--pan", type=int)
    args = parser.parse_args()
    action = args.action

    if action in ["clearing", "void"]:
        request_body = _construct_clearing_void_call(args)
    else:
        request_body = _construct_authorize_return_call(args)

    try:
        simulate(api_key, action, request_body)
    except requests.exceptions.HTTPError as e:
        print(f"Simulate failed: {e.response.text}")
