import argparse
import json

from lithic import APIError

from util import create_client

VALID_ACTIONS = [
    "authorize",
    "clearing",
    "return",
    "void",
]


def simulate(action: str, args):
    if action in ["authorize", "return"] and not args.pan:
        raise ValueError(
            "A PAN is required when simulating an authorization or a return"
        )
    if action in ["clearing", "void"] and not args.token:
        raise ValueError(
            "A transaction token is required when simulating a clearance or a void"
        )

    client = create_client()

    if action == "authorize":
        result = client.transactions.simulate_authorization(
            amount=args.amount,
            descriptor=args.descriptor,
            pan=args.pan,
        )
    elif action == "return":
        result = client.transactions.simulate_return(
            amount=args.amount,
            descriptor=args.descriptor,
            pan=args.pan,
        )
    elif action == "clearing":
        if args.amount is None:
            result = client.transactions.simulate_clearing(token=args.token)
        else:
            result = client.transactions.simulate_clearing(token=args.token, amount=args.amount)
    elif action == "void":
        if args.amount is None:
            result = client.transactions.simulate_void(token=args.token)
        else:
            result = client.transactions.simulate_void(token=args.token, amount=args.amount)
    else:
        raise ValueError(f"Unknown action: {action}")

    print(json.dumps(result.model_dump(), default=str))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("action", type=str, choices=VALID_ACTIONS)
    parser.add_argument("--token", type=str)
    parser.add_argument("--amount", type=int, default=None)
    parser.add_argument("--descriptor", type=str, default="Sample descriptor")
    parser.add_argument("--pan", type=str)
    args = parser.parse_args()

    try:
        simulate(args.action, args)
    except APIError as e:
        print(f"Simulate failed: {e}")
