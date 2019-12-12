#!/usr/bin/python3

# Use the exchangeratesapi.io to perform currency conversions.
# https://api.exchangeratesapi.io/latest?base=EUR&symbols=USD

import urllib.request

VALID_CURRENCIES = ['USD', 'EUR', 'GBP', 'AUD', 'CAD',
                    'CNY', 'ILS', 'MXN', 'RUB', 'THB', 'BRL']

class Currency:
    def __init__(self, amount=1.0, currency_type='EUR'):
        # a quick and easy way of checking for valid currencies
        # for a limited subset of valid currencies
        self.numbers = "0123456789."
        if currency_type in VALID_CURRENCIES:
            self.amount = float(amount)
            self.currency_type = currency_type
        else:
            print("Invalid currency type: %s\n", currency_type)
            self.amount = 0.0
            self.currency_type = ''

    def convert_to(self, new_currency_type):
        if new_currency_type == self.currency_type:
            # nothing to do
            return Currency(self.amount, self.currency_type)

        if new_currency_type not in VALID_CURRENCIES or self.currency_type not in VALID_CURRENCIES:
            print("Converstion from %s to %s not allowed" % (self.currency_type, new_currency_type))
            return

        # prepare URL
        url = "https://api.exchangeratesapi.io/latest?base="
        url += self.currency_type
        url += "&symbols=" + new_currency_type
        conv = urllib.request.urlopen(url)
        # read() returns an array of bytes, we want a string
        response = str(conv.read())
        a = 0
        string = ""

        while a < 25:
            if response[a] in self.numbers:
                string = string + response[a]
            a = a + 1

        exchange_rate = float(string)

        amount = self.amount * exchange_rate
        return Currency(amount, new_currency_type)

    def __str__(self):
        return str(self.amount)[:3] + "0 " + self.currency_type

    #def __repr__(self):

    def __add__(self, other_curr):

        if type(other_curr) == int:
            other_curr = self.amount + float(other_curr)
            return str(other_curr)[:4] + "0 " + self.currency_type
        elif type(other_curr) == float:
            other_curr = self.amount + other_curr
            return str(other_curr)[:4] + "0 " + self.currency_type
        else:
            new_curr1 = other_curr.convert_to(self.currency_type)
            new_curr1.amount = self.amount + new_curr1.amount
            return str(new_curr1.amount)[:4] + " " + new_curr1.currency_type

    def __sub__(self, other_curr):

        if type(other_curr) == int:
            other_curr = self.amount - float(other_curr)
            return str(other_curr)[:4] + "0 " + self.currency_type
        elif type(other_curr) == float:
            other_curr = self.amount - other_curr
            return str(other_curr)[:4] + "0 " + self.currency_type
        else:
            new_curr1 = other_curr.convert_to(self.currency_type)
            new_curr1.amount = self.amount - new_curr1.amount
            return str(new_curr1.amount)[:4] + " " + new_curr1.currency_type

    def __radd__(self, other_curr):
        return self.__add__(other_curr)

    def __rsub__(self, other_curr):
        return self.__sub__(other_curr)

    def __gt__(self, other_curr):

        if type(other_curr) == int:
            if self.amount > other_curr:
                return True
            else:
                return False
        elif type(other_curr) == float:
            if self.amount > other_curr:
                return True
            else:
                return False
        else:
            new_curr2 = other_curr.convert_to(self.currency_type)
            if self.amount > new_curr2.amount:
                return True
            else:
                return False


curr = Currency(7.50, 'USD')
print(curr)  # 7.50 USD
curr2 = Currency(2, 'EUR')
print(curr2)  # 2.00 EUR
new_curr = curr2.convert_to(curr.currency_type)  # 2.000000 EUR => 2.211600 USD
print(new_curr)  # 2.21 USD
sum_curr = curr + curr2  # 2.000000 EUR => 2.211600 USD
print(sum_curr)  # 9.71 USD
sum_curr2 = curr + 5.5
print(sum_curr2)  # 13.00 USD
sum_curr3 = curr + 3
print(sum_curr3)  # 10.50 USD
sum_curr4 = 7.3 + curr2
print(sum_curr4)
sub_curr = curr2 - 1.5
print(sub_curr)
sub_curr2 = 9.45 - curr
print(sub_curr2)
if curr > curr2:
    print(curr)
else:
    print(curr2)

if curr > 10:
    print(curr)
else:
    print(10)

if curr2 > 1.5:
    print(curr2)
else:
    print(1.5)
