"""
Expects the user to specify as a command-line argument the number of Bitcoins, n, 
that they would like to buy. If that argument cannot be converted to a float, 
the program should exit via sys.exit with an error message.

Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, 
which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...
Outputs the current cost of 
n
 Bitcoins in USD to four decimal places, using , as a thousands separator.

"""

import requests
import sys
import json

if len(sys.argv) != 2:
    print("Missing command-line argument.")
    sys.exit()
else:
    try:
        qty = float(sys.argv[1])
        try:
            price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            result = qty * price.json()["bpi"]["USD"]["rate_float"]
        except requests.RequestException:
            print("An API error occurred. Please try running again.")
            sys.exit()

        print(f"{result:,.4f}")

    except:
        print("Command-line argument is not a number.")
        sys.exit()
