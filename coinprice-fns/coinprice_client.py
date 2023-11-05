import os
import click
import requests

@click.command()
@click.option("--coin", default="bitcoin")
def get_coin_price(coin):
    headers = {"X-Github-Token": os.environ.get("COINPRICE_TOKEN")}
    url = f'https://fuzzy-lamp-6q749qjq5p4f4v95-7071.app.github.dev/api/coinprice?coin={coin}'
    data = requests.get(url, headers=headers).json()    
    print(data[coin])

if __name__ == '__main__':
    get_coin_price()

