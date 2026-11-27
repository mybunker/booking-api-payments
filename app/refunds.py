REFUND_PERIOD_DAYS = 45


def partial_refund(total_cents, refunded_cents, requested_cents, days_since_payment):
    # The period comes first: a late request is refused whatever amount it asks for.
    if days_since_payment > REFUND_PERIOD_DAYS:
        raise ValueError("Refund period expired")
    if requested_cents <= 0 or requested_cents > total_cents - refunded_cents:
        raise ValueError("Invalid refund amount")
    return requested_cents
