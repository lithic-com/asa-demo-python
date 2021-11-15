import json

import requests

from util import read_api_key


def create_card(api_key: str):
    resp = requests.post(
        "https://sandbox.lithic.com/v1/card",
        headers={"Authorization": f"api-key {api_key}"},
        json={
            "type": "UNLOCKED",
        },
    )
    resp.raise_for_status()
    print(json.dumps(resp.json()))


if __name__ == "__main__":
    api_key = read_api_key()
    try:
        create_card(api_key)
    except requests.exceptions.HTTPError as e:
        print(f"Failed to create card: {e.response.text}")
