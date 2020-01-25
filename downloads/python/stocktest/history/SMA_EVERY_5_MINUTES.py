import robin_stocks as r
from statistics import mean
from datetime import date
from datetime import datetime


login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "SPY"
time_frame = 'day'
n = 4
bounds = 'extended'
open_p = 'open_price'
close_p = 'close_price'
high_p = 'high_price'
low_p = 'low_price'

def historical_sma(value):
    day = date.today()
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    historical_sma = open("historical_sma.txt", "r")
    txt = ('{'+ '"time": "'+ str(time) +'"}, ''{'+ '"'+ str(day)  +'": "'+ str(value) +'"},' + '\n')
    readFile = historical_sma.readlines()
    readFile.insert(1, txt)
    historical_sma.close()
    historical_sma = open("historical_sma.txt", "w")
    historical_sma.writelines(readFile)
    historical_sma.close()

def loopStockInfo(open_p, stock_data):
    # open_p = category of info like high_price, low_price
    info = [sub[open_p] for sub in stock_data]
    info = [i for i in info]
    return info

def closingPrice():
    # closing price in 5 entries for SPY
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    close_p = close_p[-n:]
    return(close_p)


def current_price():
    # current price for SPY
    current_stock_price = r.get_latest_price(stock)
    current_stock_price = current_stock_price[0]
    return(current_stock_price)

def sma():
    # Simple Moving average
    close_p = closingPrice()
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    average = mean(close_p)
    average = round(average, 2)
    value = average
    historical_sma(value)
    return(average)

sma()