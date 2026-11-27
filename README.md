# booking-api

The backend of the booking app: bookings, payments and refunds.

## Tests

From the root of the repo:

    python3 -m unittest discover -s tests

This runs every test file in `tests/`. Plain `python3 -m unittest` finds no
tests, and naming one module skips the others, both without an error.

## Database

The production database is `booking-prod`.
