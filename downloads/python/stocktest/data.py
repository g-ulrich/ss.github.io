import robin_stocks as r
from statistics import mean
from robin_stocks import *
import numpy as np
import tulipy as ti

# LIST
# is a collection which is ordered and changeable. Allows duplicate members.
# list = ["apple", "banana", "cherry"]
#   print(list)
#
# TUPLE
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# tuple = ("apple", "banana", "cherry")
#   print(tuple)
#
# SET
# Set is a collection which is unordered and unindexed. No duplicate members.
# set = {"apple", "banana", "cherry"}
#   print(set)
#
# DICTIONARY
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# dictionary =	{ "brand": "Ford", "model": "Mustang", "year": 1964}
#   print(dinctionary)


#login in
login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "SPY"
# day, week, year, 5year
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


def highPrice(n):
    # high price in 5 entries for SPY
    high_p = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    high_p = loopStockInfo(high_p, stock_data)
    high_p = high_p[-n:]
    return(high_p)

def currentHigh():
    # high price in 5 entries for SPY
    high_p = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    high_p = loopStockInfo(high_p, stock_data)
    high_p = high_p[:1]
    return(high_p)

def currentLow():
    # high price in 5 entries for SPY
    low_p = 'low_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    low_p = loopStockInfo(low_p, stock_data)
    low_p = low_p[:1]
    return(low_p)

def lowPrice(n):
    # low price in 5 entries for SPY
    low_p = 'low_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    low_p = loopStockInfo(low_p, stock_data)
    low_p = low_p[-n:]
    return(low_p)


def openPrice():
    # open price in 5 entries for SPY
    open_p = 'open_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    open_p = loopStockInfo(open_p, stock_data)
    open_p = open_p[-n:]
    return(open_p)

def closingPrice():
    # closing price in 5 entries for SPY
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
    close_p = loopStockInfo(close_p, stock_data)
    close_p = close_p[-n:]
    return(close_p)

def current_price():
    # current price for SPY
    current_stock_price = r.get_latest_price(stock)
    current_stock_price = current_stock_price[0]
    return(current_stock_price)

def myCash():
    # my available cash
    my_cash = r.build_user_profile()
    my_cash = my_cash.get("cash")
    return(my_cash)

def sma():
    # Simple Moving average
    close_p = closingPrice()
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    print(close_p)
    average = mean(close_p)
    average = round(average, 2)
    return(average)


prices = 'high_price'
time_frame = 'day'
stock_data = r.get_historicals(stock, span=time_frame, bounds='regular')
prices = loopStockInfo(prices, stock_data)
prices = [float(i) for i in prices]
prices = np.asarray(prices)
sma = ti.sma(prices, period=5)
sma = mean(sma[-5:])
print(sma)


# print_info(ti.sma)