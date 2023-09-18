from endpoints import HuobiDM
import requests
import os
from environs import Env
env = Env()
env.read_env('.env')
ACCESS_KEY = (env("ACCESS_KEY"))
SECRET_KEY = (env("SECRET_KEY"))
invest = 2

# huobi dm url

URL = 'https://api.hbdm.com'
#'http://api.hbdm.vn'
#'https://api.hbdm.com'

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

def get_price(symbol):
    try:
        url = f'https://api.huobi.pro/market/trade?symbol={symbol}'
        res = requests.get(url)
        return res.json()
    except Exception as z:
        print("price", z)
        return None
        
def long_trade(coin):
    symbol = coin.lower()
    price = get_price(f"{symbol}usdt")['tick']['data'][0]['price']
    print("price", price)
    cont_size = dm.swap_contract_info(f'{coin}-USDT')['data'][0]['contract_size']
    print("cont_size", cont_size)
    intendedAmount = invest*10
    print("intendedAmount", intendedAmount)
    csp = cont_size*price
    print("csp", csp)
    volume = int(intendedAmount / csp)
    print("volume", volume)
    decimals = len(str(price).split('.')[1])
    if decimals == 2:
        decimals = 1
    inc = 0.05 * price
    TP = price + inc
    dec = 0.07 * price
    SL = price - dec
    TP_rounded = round(TP, decimals)
    SL_rounded = round(SL, decimals)
    order = dm.linear_swap_order(f"{coin}-USDT", volume, "buy", "open", 10, TP_rounded, SL_rounded)
    print("order", order)
    status = order.get('status')
    red = f"*Order Placed*\n\n*Asset:* {coin}\n*Price:* {price}\n*TP:* {TP_rounded}\n*SL:* {SL_rounded}\n*Leverage: {10}*\n*Volume:* {5}\n\n*Status:* {status}"
    print(red)
    
def short_trade(coin):
    symbol = coin.lower()
    price = get_price(f"{symbol}usdt")['tick']['data'][0]['price']
    print("price", price)
    cont_size = dm.swap_contract_info(f'{coin}-USDT')['data'][0]['contract_size']
    print("cont_size", cont_size)
    intendedAmount = invest*10
    print("intendedAmount", intendedAmount)
    csp = cont_size*price
    print("csp", csp)
    volume = int(intendedAmount / csp)
    print("volume", volume)
    decimals = len(str(price).split('.')[1])
    if decimals == 2:
        decimals = 1
    inc = 0.07 * price
    SL = price + inc
    dec = 0.05 * price
    TP = price - dec
    TP_rounded = round(TP, decimals)
    SL_rounded = round(SL, decimals)
    order = dm.linear_short_order(f"{coin}-USDT", volume, "sell", "open", 10, TP_rounded, SL_rounded)
    print("order", order)
    status = order.get('status')
    red = f"*Order Placed*\n\n*Asset:* {coin}\n*Price:* {price}\n*TP:* {TP_rounded}\n*SL:* {SL_rounded}\n*Leverage: {10}*\n*Volume:* {5}\n\n*Status:* {status}"
    print(red)


def close(coin, direction):
    symbol = coin.lower()
    price = get_price(f"{symbol}usdt")['tick']['data'][0]['price']
    print("price", price)
    cont_size = dm.swap_contract_info(f'{coin}-USDT')['data'][0]['contract_size']
    print("cont_size", cont_size)
    intendedAmount = invest*10
    print("intendedAmount", intendedAmount)
    csp = cont_size*price
    print("csp", csp)
    volume = int(intendedAmount / csp)
    close = dm.linear_closing(f"{coin}-USDT", volume, direction, "close", 10)
    print(close)
    status = close.get('status')
    if status == 'ok':
        return "Trade Canceled"
    else:
        return "Sorry! No trade open for this Pair"
