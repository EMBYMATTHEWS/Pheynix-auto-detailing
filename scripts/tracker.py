#!/usr/bin/env python3
"""
Pheynix Investment Tracker
Fetches crypto prices and updates tracking log
"""
import urllib.request
import json
from datetime import datetime

def get_crypto_prices():
    """Fetch BTC and ETH prices from CoinGecko API"""
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
    response = urllib.request.urlopen(url, timeout=5)
    data = json.loads(response.read().decode())
    return {
        'bitcoin': data['bitcoin']['usd'],
        'ethereum': data['ethereum']['usd'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

def update_log(prices):
    """Append prices to tracking log"""
    import os
    log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'investment-log.txt')
    with open(log_path, 'a') as f:
        f.write(f"{prices['timestamp']} | BTC: ${prices['bitcoin']} | ETH: ${prices['ethereum']}\n")
    print(f"Prices logged to {log_path}")

if __name__ == '__main__':
    prices = get_crypto_prices()
    print(f"Bitcoin: ${prices['bitcoin']}")
    print(f"Ethereum: ${prices['ethereum']}")
    update_log(prices)
