import unittest

from app.refunds import partial_refund


class RefundWithinThirtyDays(unittest.TestCase):
    def test_returns_the_requested_amount(self):
        self.assertEqual(partial_refund(10000, 0, 4000, 10), 4000)

    def test_allows_the_whole_remainder(self):
        self.assertEqual(partial_refund(10000, 2500, 7500, 0), 7500)

    def test_allows_one_cent(self):
        self.assertEqual(partial_refund(10000, 9999, 1, 29), 1)

    def test_allows_day_thirty(self):
        self.assertEqual(partial_refund(10000, 0, 4000, 30), 4000)


class RefundAfterThirtyDays(unittest.TestCase):
    def assertExpired(self, *args):
        with self.assertRaisesRegex(ValueError, "Refund period expired"):
            partial_refund(*args)

    def test_refuses_day_thirty_one(self):
        self.assertExpired(10000, 0, 4000, 31)

    def test_refuses_day_forty_five(self):
        self.assertExpired(10000, 0, 4000, 45)

    def test_refuses_late_request_even_with_invalid_amount(self):
        self.assertExpired(10000, 0, 0, 31)


class InvalidAmount(unittest.TestCase):
    def assertInvalid(self, *args):
        with self.assertRaisesRegex(ValueError, "Invalid refund amount"):
            partial_refund(*args)

    def test_zero(self):
        self.assertInvalid(10000, 0, 0, 10)

    def test_negative(self):
        self.assertInvalid(10000, 0, -100, 10)

    def test_more_than_the_remainder(self):
        self.assertInvalid(10000, 2500, 7501, 10)

    def test_already_fully_refunded(self):
        self.assertInvalid(10000, 10000, 1, 10)


if __name__ == "__main__":
    unittest.main()
