# -*- coding: utf-8 -*-
import os
import json

import requests
from flask import Flask

app = Flask(__name__)

LINE_NOTIFY_TOKEN = os.environ.get('LINE_NOTIFY_TOKEN')

SBI_BASE_URL = 'https://trade.sbifxt.co.jp/api_fxt/HttpApi/ChartCache.aspx'
LINE_NOTIFY_URL = 'https://notify-api.line.me/api/notify'
LINE_NOTIFY_HEADERS = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}

parameter = {
    'CURID': 'USDJPY',
    'TIMESCALE': 1,
    'COUNT': 1,
    'DEVICE': 'PCWebFXAUTO',
    'GUID': '$2a$10$I/8SDPJdiyr3SlyS9h6N8eBLTKk4NN8ribqrTbYND.RpH.GzE4MMi'
}

@app.route("/usdjpy")
def hello():
    market_info = requests.post(SBI_BASE_URL, parameter).text.split()
    currency_pair = market_info[3]
    bid_price = float(market_info[4])
    if currency_pair == 'USDJPY':
        message_data = {'message': f'\n USD-JPY: {bid_price:.3f}'}
        requests.post(LINE_NOTIFY_URL, headers = LINE_NOTIFY_HEADERS, data = message_data)
    return "notification app!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)