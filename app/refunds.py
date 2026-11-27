def partial_refund(total_cents, refunded_cents, requested_cents, days_since_payment):
    if requested_cents <= 0 or requested_cents > total_cents - refunded_cents:
        raise ValueError("Invalid refund amount")
    # The rule past 30 days is not implemented yet.
    return requested_cents
