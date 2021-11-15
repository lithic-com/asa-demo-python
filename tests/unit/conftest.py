import pytest


@pytest.fixture
def mock_asa_request():
    return {
        "token": "7842e70e-2b17-47ca-8541-869636bedf6a",
        "status": "AUTHORIZATION",
        "pos": {
            "terminal": {
                "attended": False,
                "operator": "CARDHOLDER",
                "on_premise": True,
                "card_retention_capable": False,
                "pin_capability": "UNSPECIFIED",
                "type": "ECOMMERCE",
                "partial_approval_capable": False,
            },
            "entry_mode": {
                "pan": "KEY_ENTERED",
                "pin_entered": False,
                "cardholder": "MAIL_ORDER",
                "card": "NOT_PRESENT",
            },
        },
        "settled_amount": 0,
        "created": "2021-11-14T15:20:08Z",
        "amount": 52,
        "acquirer_fee": 0,
        "authorization_amount": 52,
        "card": {
            "token": "76b9f589-8935-4e78-8809-7f583bf0fb89",
            "hostname": "",
            "last_four": "3860",
            "state": "OPEN",
            "type": "UNLOCKED",
            "memo": "UNLOCKED card",
            "spend_limit": 0,
            "spend_limit_duration": "TRANSACTION",
        },
        "merchant": {
            "descriptor": "coffee shop",
            "city": "NEW YORK",
            "state": "NY",
            "country": "USA",
            "acceptor_id": "174030075991",
            "mcc": "5812",
        },
        "avs": {"zipcode": "33090", "address": None},
        "events": [],
        "funding": [],
    }
