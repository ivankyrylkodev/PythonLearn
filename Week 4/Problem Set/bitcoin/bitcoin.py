import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=93eaf841343042f41796be257d3eb6373f0d65e303f0a1138e3fdb0811d6a22f")
    o = response.json()
    result = float(o["data"]["priceUsd"]) * float(sys.argv[1])
    print(f"${result:,.4f}")
except requests.RequestException:
    sys.exit("Error")
except ValueError:
    sys.exit("Command-line argument is not a number")
    