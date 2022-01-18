import pytest

from currencyConverter import Currency_convertor

YOUR_ACCESS_KEY = 'd6b399c7897e6895310c3ee916fc6635'
url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
c = Currency_convertor(url)


def test_api():
    try:
        # trying to get the rates, if we get it the --> api works well
        c.rates
    except:
        pytest.fail("api doesn't work")


def test_rates():
    rates = {}
    try:
        rates = c.rates_test()
    except:
        pytest.fail("shouldn't happen")
    assert len(rates) != 0


def test_convert():
    try:
        euro_to_rub = c.convert("EUR", "RUB", 100)
        rub_to_euro = c.convert("RUB", "EUR", euro_to_rub)
    except:
        pytest.fail("shouldn't happen")

    assert euro_to_rub > 0
    assert rub_to_euro == 100

