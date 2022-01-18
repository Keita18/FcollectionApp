# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

        # function to do a simple cross multiplication between

    def rates_test(self):
        return self.rates

    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        return amount


# Driver code
if __name__ == "__main__":

    YOUR_ACCESS_KEY = 'd6b399c7897e6895310c3ee916fc6635'
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
    c = Currency_convertor(url)

    flag = True

    while flag:
        print('==================================')
        from_country = input("From Country: ")
        if from_country == '-exit':
            flag = False
            continue
        to_country = input("TO Country: ")
        amount = int(input("Amount: "))

        c.convert(from_country, to_country, amount)
