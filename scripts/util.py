import os

from lithic import Lithic


def create_client() -> Lithic:
    api_key = os.environ.get("LITHIC_API_KEY") or os.environ.get("LITHIC_SANDBOX_KEY")
    if not api_key:
        print(
            "\033[93mYou can set the LITHIC_API_KEY environment variable to avoid entering this each time!\033[0m"
        )
        api_key = input("Enter your Lithic Sandbox API Key: ")

    return Lithic(api_key=api_key, environment="sandbox")
