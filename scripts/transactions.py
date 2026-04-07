import json

from lithic import APIError

from util import create_client


def list_transactions():
    client = create_client()
    transactions = client.transactions.list()
    print(json.dumps([t.model_dump() for t in transactions], default=str))


if __name__ == "__main__":
    try:
        list_transactions()
    except APIError as e:
        print(f"Failed to list transactions: {e}")
