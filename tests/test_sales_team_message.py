import unittest

from demo_app.invoice import validate
from tests.invoices import invoice


class TestTheRefusal(unittest.TestCase):
    def test_says_to_add_a_sales_person_in_the_sales_team_table(self):
        try:
            validate(invoice())
        except ValueError as e:
            self.assertIn("Add at least one Sales Person in the Sales Team table", str(e))
        else:
            self.fail("an invoice without a Sales Team row was accepted")
