import unittest

from demo_app.invoice import validate
from tests.invoices import invoice


class TestAnInvoiceWithoutASalesTeamRow(unittest.TestCase):
    def test_is_refused(self):
        with self.assertRaises(ValueError):
            validate(invoice())

    def test_with_one_sales_person_is_accepted(self):
        validate(invoice(sales_team=[{"sales_person": "Asha"}]))
