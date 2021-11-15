import argparse

import requests

from util import read_api_key


def enroll_asa(api_key: str, webhook_url: str):
    resp = requests.post(
        "https://sandbox.lithic.com/v1/authstream/enroll",
        headers={
            "Authorization": f"api-key {api_key}",
            "Content-type": "application/json",
        },
        json={
            "webhook_url": webhook_url,
        },
    )
    resp.raise_for_status()
    print("\033[92mSuccessfully enrolled\033[0m")


if __name__ == "__main__":
    api_key = read_api_key()
    parser = argparse.ArgumentParser()
    parser.add_argument("webhook_url", type=str)
    args = parser.parse_args()

    try:
        enroll_asa(api_key, args.webhook_url)
    except requests.exceptions.HTTPError as e:
        print(f"Failed to enroll webhook: {e.response.text}")
