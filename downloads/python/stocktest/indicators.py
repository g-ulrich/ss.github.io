import pandas as pd
import robin_stocks as r
import numpy as np
from statistics import mean

from stockstats import StockDataFrame

login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "SPY"

time_frame = 'day'
n = 5
# regular extended
bounds = 'extended'
open_p = 'open_price'
close_p = 'close_price'
high_p = 'high_price'
low_p = 'low_price'
volume = 'volume'

def loopStockInfo(open_p, stock_data):
    # open_p = category of info like high_price, low_price
    info = [sub[open_p] for sub in stock_data]
    info = [i for i in info]
    return info

def volume_now():
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [int(i) for i in volume]
    result = sum(result[-1:])
    return (result)

def volume_n(n):
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [int(i) for i in volume]
    result = sum(result[-n:])
    return (result)

def volume_list():
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [float(i) for i in volume]
    # result = result[-n:]
    return (result)

def volume_today():
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [int(i) for i in volume]
    return (result)

def closingPrice():
    # closing price in 5 entries for SPY
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    close_p = close_p[-n:]
    return(close_p)

def closing_n_price(n):
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    close_p = close_p[-n:]
    return(close_p)

def high_n_Price(n):
    high_p = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    high_p = loopStockInfo(high_p, stock_data)
    high_p = high_p[-n:]
    return(high_p)

def current_price():
    # current price for SPY
    current_stock_price = r.get_latest_price(stock)
    current_stock_price = current_stock_price[0]
    return(current_stock_price)

def closing_price_n_days(n):
    close_p = 'close_price'
    time_frame = 'day'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    close_p = close_p[-n:]
    return (close_p)

def close_price_n_with_current_price(n):
    close_p = closing_n_price(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    result = [float(i) for i in close_p][-n:]
    return(result)

def sma():
    # Simple Moving average
    n = 5
    close_p = closing_n_price(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    average = mean(close_p)
    average = round(average, 2)
    return(average)

def sma_n_day(n):
    # Simple Moving average
    close_p = closing_price_n_days(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    close_p = mean(close_p)
    average = close_p
    average = round(average, 2)
    return(average)

def ema(n):
    #  EMA = Price(t) * k + EMA(y) * (1 – k)
    #  EMA = smooth * current_price + (1 - smooth) * sma_n_day(n)
    smooth = float((2 / (n + 1)))
    ema_calc = (float(current_price()) * smooth) + sma_n_day(n) * (1-smooth)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * sma_n_day(n)
    ema_calc = round(ema_calc, 2)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * ema_calc
    ema_calc = round(ema_calc, 2)
    return(ema_calc)

def gain_value(gain):
    file_path = "history/rsi/temp_gains.txt"
    file = open(file_path, "r")
    txt = (str(gain) +'\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def loss_value(loss):
    file_path = "history/rsi/temp_losses.txt"
    file = open(file_path, "r")
    txt = (str(loss) +'\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def gain_loss(close, c1, c2):
    c2 = c2 + 1
    change = close[-c1] - close[-c2]
    gain = change if change > 0 else 0
    gain_value(gain)
    loss = abs(change) if change < 0 else 0
    loss_value(loss)

def gain_value_avg(close, c1):
    c2 = c1 + 1
    change = close[-c1] - close[-c2]
    gain = change if change > 0 else 0
    return(gain)

def loss_value_avg(close, c1):
    c2 = c1 + 1
    change = close[-c1] - close[-c2]
    loss = abs(change) if change < 0 else 0
    return(loss)

def gains_loss_data_float_avg(data):
    data = [line.rstrip('\n') for line in open(data)]
    result = [float(i) for i in data]
    result = mean(result)
    return(result)

def close_data(n):
    result = [float(i) for i in closing_n_price(n)]
    return(result)

def rsi():
    n = 14
    records = 20
    loop = 1
    one_less = n - 1
    n_loop = n + 1
    three_more = n + 3
    gains_data = "history/rsi/temp_gains.txt"
    losses_data = "history/rsi/temp_losses.txt"
    close = close_price_n_with_current_price(records)
    nxt_gain_value = gain_value_avg(close, three_more)
    nxt_loss_value = loss_value_avg(close, three_more)
    open(gains_data, 'w').close()
    open(losses_data, 'w').close()
    while loop < n_loop:
        gain_loss(close, loop, loop)
        loop += 1
    avg_gain = gains_loss_data_float_avg(gains_data)
    avg_loss = gains_loss_data_float_avg(losses_data)
    avg_gain = (one_less * avg_gain + nxt_gain_value) / n
    avg_loss = (one_less * avg_loss + nxt_loss_value) / n
    rs = avg_gain / avg_loss
    rsi = round(100 - (100 / (rs + 1)), 2)
    return(rsi)

def smoothing(n):
    result = round(float((2 / (n + 1))), 2)
    return(result)

def rsiFunc(n=14):
    prices = close_price_n_with_current_price(n)
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed >= 0].sum()/n
    down = -seed[seed < 0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)
    for i in range(n, len(prices)):
        delta = deltas[i-1]
        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)
    rsi = rsi.tolist()
    rsi = [float(i) for i in rsi]
    rsi = round(rsi[0], 2)
    return(rsi)

def avg_rsi():
    result = (rsi() + rsiFunc()) / 2
    result = round(result, 2)
    return(result)

def macd():
    fast_n = 12
    slow_n = 26
    signal_n = 9
    fast_ema = smoothing(fast_n)
    slow_ema = smoothing(slow_n)
    signal = smoothing(signal_n)
    close_fast_ema = close_price_n_with_current_price(fast_n)
    close_slow_ema = close_price_n_with_current_price(slow_n)
    close_signal = close_price_n_with_current_price(signal_n)
    fast_ema_n = round(mean(close_fast_ema), 2)
    slow_ema_n = round(mean(close_slow_ema), 2)
    signal_n = round(mean(close_signal), 2)
    fast_ema_calc = round(((close_price_n_with_current_price(fast_n + 1)[0] - fast_ema_n) * fast_ema) + fast_ema_n, 2)
    slow_ema_calc = round(((close_price_n_with_current_price(slow_n + 1)[0] - slow_ema_n) * slow_ema) + slow_ema_n, 2)
    diff = fast_ema_calc - slow_ema_calc
    return(diff)

def vwap_to_temp(n, loop):
    volxclose = sum(close_price_n_with_current_price(n)[-loop:]) * sum(volume_list()[-loop:])
    file_path = "history/temp.txt"
    file = open(file_path, "r")
    txt = (str(volxclose) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def write_first_line(tmp_file):
    file_path = tmp_file
    file = open(file_path, "r")
    txt = ("DontDelete" + "\n")
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def volxclose_data_float():
    data = "history/temp.txt"
    data = [line.rstrip('\n') for line in open(data)]
    data.remove(data[0])
    result = [float(i) for i in data]
    return(result)

def rsi_output():
    if str(current_price()) < str(ema(5)):
        result = rsi()
    elif str(current_price()) == str(ema(5)):
        result = avg_rsi()
    else:
        result = rsiFunc()
    return(result)
#
# # def vwap():
# prices = 'high_price'
# stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
# prices = loopStockInfo(prices, stock_data)
# prices = [float(i) for i in prices]
# high_p = prices[-1:]
#
# prices = 'low_price'
# stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
# prices = loopStockInfo(prices, stock_data)
# prices = [float(i) for i in prices]
# low_p = prices[-1:]
#
# prices = 'close_price'
# stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
# prices = loopStockInfo(prices, stock_data)
# prices = [float(i) for i in prices]
# close_p = prices[-1:]
#
# volumexclose = sum(close_p) * volume_now()
# # vwap_13 = volume_n(13) /
#
#
#
#
# n = 13
# loop = 1
# n_loop = n + 1
# tmp_file = "history/temp.txt"
# open(tmp_file, 'w').close()
# write_first_line(tmp_file)
# while loop < n_loop:
#     vwap_to_temp(n, loop)
#     loop += 1
# volxclose = sum(volxclose_data_float())
# vwap_13 = volxclose / volume_n(n)
# print(vwap_13)



#
# typical_price = high_p + low_p + close_p
# typical_price = mean(typical_price)
# first = typical_price + volume_now()
# second = sum(volume_today())
# result = first / second
# print(volume_list())



# print("CURRENT PRICE FOR " + stock + "\n" + str(current_price()) + "\n")
# print("macd blue diff: " + str(macd()))
# print("RSI " + str(rsi_output()))
# print("sma 5: " + str(sma()))
# print("ema 20: " + str(ema(20)))
# print("ema 5: " + str(ema(5)))
# print(volume())


def current_high_Price(n=1):
    price = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    price = loopStockInfo(price, stock_data)
    price = [float(i) for i in price]
    return(sum(price[-n:]))

def current_low_Price(n=1):
    price = 'low_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    price = loopStockInfo(price, stock_data)
    price = [float(i) for i in price]
    return(sum(price[-n:]))

# -------------------------------------------------------------------------------
print(rsi())