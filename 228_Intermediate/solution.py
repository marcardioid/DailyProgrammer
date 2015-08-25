import requests

def get_bitcoin_value(market, currency):
    if not market or not currency:
        raise ValueError("Please specify an exchange market and a currency.")
    r = requests.get("http://api.bitcoincharts.com/v1/trades.csv", params={"symbol": market + currency})
    if r.ok:
        p = r.text
        return float(p.splitlines()[::-1][0].split(',')[1])
    else:
        raise ValueError("Could not find data on '{}' for '{}': {} {}".format(market.upper(), currency.upper(), r.status_code, r.reason))

if __name__ == "__main__":
    print(get_bitcoin_value("vcx", "USD"), "USD")