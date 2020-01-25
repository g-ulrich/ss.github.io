import robin_stocks as r
import numpy as np
from statistics import mean

login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "AMZN"

time_frame = 'day'
n = 5
open_p = 'open_price'
close_p = 'close_price'
high_p = 'high_price'
low_p = 'low_price'

def ratings():
    result = r.get_ratings(stock, info=None)
    result = result['summary']
    hold = result['num_hold_ratings']
    buy = result['num_buy_ratings']
    sell = result['num_sell_ratings']
    if buy > hold and buy > sell:
        result = "Buy " + stock
    elif hold > buy and hold > sell:
        result = "Hold " + stock
    else:
        result = "Sell " + stock
    return(result)

print(ratings())