import argparse

from lithic import APIError

from util import create_client


def enroll_asa(webhook_url: str):
    client = create_client()
    client.responder_endpoints.create(
        type="AUTH_STREAM_ACCESS",
        url=webhook_url,
    )
    print("\033[92mSuccessfully enrolled\033[0m")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("webhook_url", type=str)
    args = parser.parse_args()

    try:
        enroll_asa(args.webhook_url)
    except APIError as e:
        print(f"Failed to enroll webhook: {e}")
