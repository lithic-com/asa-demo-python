from lithic import APIError

from util import create_client


def disenroll_asa():
    client = create_client()
    client.responder_endpoints.delete(type="AUTH_STREAM_ACCESS")
    print("\033[92mSuccessfully disenrolled\033[0m")


if __name__ == "__main__":
    try:
        disenroll_asa()
    except APIError as e:
        print(f"Failed to disenroll: {e}")
