import pytest

from lithic.types import CardAuthorizationApprovalRequestWebhookEvent
from lithic.types.card_authorization_approval_request_webhook_event import (
    Avs,
    Card,
    Merchant,
)


def make_merchant(mcc="5812", state="NY"):
    return Merchant.model_construct(
        mcc=mcc,
        state=state,
        descriptor="coffee shop",
        city="NEW YORK",
        country="USA",
        acceptor_id="174030075991",
        acquiring_institution_id="",
    )


@pytest.fixture
def mock_asa_request():
    return CardAuthorizationApprovalRequestWebhookEvent.model_construct(
        token="7842e70e-2b17-47ca-8541-869636bedf6a",
        status="AUTHORIZATION",
        event_type="card_authorization.approval_request",
        settled_amount=0,
        created="2021-11-14T15:20:08Z",
        amount=52,
        acquirer_fee=0,
        authorization_amount=52,
        merchant_amount=52,
        merchant_currency="USD",
        cardholder_currency="USD",
        cash_amount=0,
        transaction_initiator="CARDHOLDER",
        amounts=None,
        card=Card.model_construct(
            token="76b9f589-8935-4e78-8809-7f583bf0fb89",
            last_four="3860",
            state="OPEN",
            type="UNLOCKED",
            memo="UNLOCKED card",
        ),
        merchant=make_merchant(),
        avs=Avs.model_construct(
            zipcode="33090",
            address=None,
        ),
    )
