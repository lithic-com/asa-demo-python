from lithic.types import CardAuthorizationApprovalRequestWebhookEvent
from lithic.types.card_authorization_approval_request_webhook_event import Merchant

APPROVED_RESULT = "APPROVED"
UNAUTHORIZED_RESULT = "UNAUTHORIZED_MERCHANT"
# 5933: Pawn shops
# 5945: Game, Toy and Hobby Shops
DISALLOWED_MCCS = ["5933", "5945"]
# For some reason, we are going to disallow Connecticut
DISALLOWED_MERCHANT_STATES = ["CT"]


def authorize_merchant(merchant: Merchant) -> bool:
    """
    Dummy function showing some potential auth logic around merchant logic
    """
    is_allowed_mcc = merchant.mcc not in DISALLOWED_MCCS
    is_allowed_state = merchant.state not in DISALLOWED_MERCHANT_STATES
    return is_allowed_mcc and is_allowed_state


def authorize(asa_request: CardAuthorizationApprovalRequestWebhookEvent) -> str:
    """
    Performs authorization logic, returning the authorization result.
    """
    is_authorized_merchant = authorize_merchant(asa_request.merchant)
    return APPROVED_RESULT if is_authorized_merchant else UNAUTHORIZED_RESULT
