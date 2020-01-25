import robin_stocks as r
import numpy as np
from statistics import mean

login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "SPY"
time_frame = 'day'
n = 5
open_p = 'open_price'
close_p = 'close_price'
high_p = 'high_price'
low_p = 'low_price'

def loopStockInfo(open_p, stock_data):
    # open_p = category of info like high_price, low_price
    info = [sub[open_p] for sub in stock_data]
    info = [i for i in info]
    return info

def closingPrice():
    # closing price in 5 entries for SPY
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='extended')
    close_p = loopStockInfo(close_p, stock_data)
    # close_p = close_p[-n:]
    return(close_p)

def current_price():
    # current price for SPY
    result = r.get_latest_price(stock)
    result = result[0]
    print_to_temp(result)
    return(result)

def price_data_float_n(n):
    data = "price/price_temp.txt"
    data = [line.rstrip('\n') for line in open(data)]
    data.remove(data[0])
    result = [float(i) for i in data]
    result = result[:n]
    return(result)

def print_to_temp(n):
    file_path = "price/price_temp.txt"
    file = open(file_path, "r")
    txt = (str(n) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def close_data():
    result = [float(i) for i in closingPrice()]
    return(result)

print(price_data_float_n(13))