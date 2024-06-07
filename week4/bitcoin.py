import sys
import json
import requests


def main():
    try:
        number_of_coins = float(sys.argv[1])
    except IndexError:
        sys.exit('Missing command-line argument')
    except ValueError:
        sys.exit('Command-line argument is not a number')
    btc_price = get_btc_price()
    amount = btc_price * number_of_coins
    print(f'${amount:,.4f}')


def request_with_retry(url, n):
    if n > 0:
        try:
            return requests.get(url)
        except requests.RequestException:
            return request_with_retry(url, n - 1)
    return None


def get_btc_price():
    res = request_with_retry('https://api.coindesk.com/v1/bpi/currentprice.json', 3)
    if res is None:
        sys.exit('Could not get data')
    try:
        res = res.json()
    except json.decoder.JSONDecodeError:
        sys.exit('Received data is not a valid JSON')
    try:
        btc_price = res['bpi']['USD']['rate_float']
    except KeyError:
        sys.exit('Received data in invalid format')
    return btc_price


if __name__ == '__main__':
    main()
