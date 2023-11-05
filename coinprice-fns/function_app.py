import azure.functions as func
import datetime
import json
import logging
import requests
import json

app = func.FunctionApp()

@app.route(route="coinprice", auth_level=func.AuthLevel.ANONYMOUS)
def coinprice(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    coin = req.params.get('coin')    
    if not coin:
        coin = 'bitcoin'

    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
    data = requests.get(url).json()
    coin_price = data[coin]['usd']

    return func.HttpResponse(
        json.dumps({
            coin: coin_price
        }),
        mimetype="application/json"
        )
    