import unittest

from demo_app.invoice import margin_rate


class TestMarginRate(unittest.TestCase):
    def test_no_selling_price_means_no_margin(self):
        self.assertEqual(margin_rate(0, 50), 0.0)
