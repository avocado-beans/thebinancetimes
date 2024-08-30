import requests

def cmc_stats(symbol, cmc_key) -> None:
    response = requests.get(
    url='https://pro-api.coinmarketcap.com/v2/cryptocurrency/info',
    headers={
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': cmc_key,
        },
    params={
        'symbol':symbol,
        })
    message = f"Didn't find anything on ({symbol})"
    if 'data' in response.json():
        message = f"Found {len(response.json()['data'][symbol])} projects that matches the symbol ({symbol})."
        for data in response.json()['data'][symbol][:5]:
            try:
                chain = data['platform']['symbol']
                token_address = data['platform']['token_address']
                message += f"\n------------------------------\nChain: {chain}\nAddress: {token_address}"
            except:
                pass
    return message

if __name__ == "__main__":
    symbol = cmc_stats(input("Enter symbol: ").upper(), cmc_key)
