import json

from lithic import APIError

from util import create_client


def create_card():
    client = create_client()
    card = client.cards.create(type="UNLOCKED")
    print(json.dumps(card.model_dump(), default=str))


if __name__ == "__main__":
    try:
        create_card()
    except APIError as e:
        print(f"Failed to create card: {e}")
