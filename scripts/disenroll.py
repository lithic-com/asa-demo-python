import requests

from util import read_api_key


def disenroll_asa(api_key: str):
    resp = requests.post(
        "https://sandbox.lithic.com/v1/authstream/disenroll",
        headers={
            "Authorization": f"api-key {api_key}",
            "Content-type": "application/json",
        },
    )
    resp.raise_for_status()
    print("\033[92mSuccessfully disenrolled\033[0m")


if __name__ == "__main__":
    api_key = read_api_key()
    try:
        disenroll_asa(api_key)
    except requests.exceptions.HTTPError as e:
        print(f"Failed to disenroll: {e.response.text}")
