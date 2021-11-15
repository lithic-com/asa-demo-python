import os


def read_api_key():
    try:
        api_key = os.environ["LITHIC_SANDBOX_KEY"]
    except KeyError:
        print(
            "\033[93mYou can set the LITHIC_SANDBOX_KEY environment variable to avoid entering this each time!\033[0m"
        )
        api_key = input("Enter your Lithic Sandbox API Key: ")

    return api_key
