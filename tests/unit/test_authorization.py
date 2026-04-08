import pytest

from tests.unit.conftest import make_merchant

from webhook.authorization import (
    authorize,
    authorize_merchant,
    APPROVED_RESULT,
    UNAUTHORIZED_RESULT,
    DISALLOWED_MCCS,
    DISALLOWED_MERCHANT_STATES,
)

VALID_MCC = "5816"
VALID_STATE = "CA"


@pytest.mark.parametrize(
    "mcc,state,expected",
    [
        (DISALLOWED_MCCS[0], VALID_STATE, False),
        (VALID_MCC, DISALLOWED_MERCHANT_STATES[0], False),
        (VALID_MCC, VALID_STATE, True),
    ],
)
def test_authorize_merchant(mcc, state, expected):
    merchant = make_merchant(mcc=mcc, state=state)
    result = authorize_merchant(merchant)
    assert result is expected


def test_authorize(mock_asa_request):
    result = authorize(mock_asa_request)
    assert result == APPROVED_RESULT


def test_authorize_invalid(mock_asa_request):
    mock_asa_request.merchant = make_merchant(mcc=VALID_MCC, state=DISALLOWED_MERCHANT_STATES[0])
    result = authorize(mock_asa_request)
    assert result == UNAUTHORIZED_RESULT
