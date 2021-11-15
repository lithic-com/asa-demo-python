import json

import requests

from util import read_api_key


def list_transactions(api_key: str):
    resp = requests.get(
        "https://sandbox.lithic.com/v1/transaction",
        headers={
            "Authorization": f"api-key {api_key}",
            "Content-type": "application/json",
        },
    )
    resp.raise_for_status()
    print(json.dumps(resp.json()))


if __name__ == "__main__":
    api_key = read_api_key()

    try:
        list_transactions(api_key)
    except requests.exceptions.HTTPError as e:
        print(f"Failed to enroll webhook: {e.response.text}")
