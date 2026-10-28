import unittest

from demo_app.invoice import validate
from tests.invoices import invoice


class TestAReturn(unittest.TestCase):
    def test_without_a_sales_team_row_is_still_accepted(self):
        validate(invoice(is_return=1))
