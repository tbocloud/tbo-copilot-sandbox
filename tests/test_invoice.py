import unittest

from demo_app.invoice import margin_rate


class TestMarginRate(unittest.TestCase):
    def test_no_selling_price_means_no_margin(self):
        self.assertEqual(margin_rate(0, 50), 0.0)

    def test_margin_is_a_share_of_the_selling_price(self):
        self.assertAlmostEqual(margin_rate(100, 80), 0.2)
        self.assertAlmostEqual(margin_rate(50, 50), 0.0)
