import sys
import requests

if len(sys.argv) != 2: #2 elements
    sys.exit("Missing command-line argument")

try:
    amt = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0ba186e8976d9f962e08e6d8b34c6fbb04b8f921d2ada768ee7c1c5014576e3c")

    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit()

total = amt * price

print(f"${total:,.4f}")
