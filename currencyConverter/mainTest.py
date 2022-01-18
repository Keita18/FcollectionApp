import unittest
from currencyConverter import Currency_convertor


class TestApp(unittest.TestCase):
    YOUR_ACCESS_KEY = 'd6b399c7897e6895310c3ee916fc6635'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    c = Currency_convertor(url)

    def test_api(self):
        try:
            # trying to get the rates, if we get it the --> api works well
            self.c.rates
        except:
            self.fail("shouldn't happen")

    def test_rates(self):
        try:
            rates = self.c.rates_test()
        except:
            self.fail("shouldn't happen")
        self.assertTrue(rates)

    def test_convert(self):
        try:
            euro_to_rub = self.c.convert("EUR", "RUB", 100)
            rub_to_euro = self.c.convert("RUB", "EUR", euro_to_rub)
        except:
            self.fail("shouldn't happen")

        self.assertTrue(euro_to_rub > 1000)
        self.assertEqual(100, rub_to_euro)



