from math import isclose

import numpy
import pandas as pd
import robin_stocks as r
import numpy as np
from statistics import mean
from datetime import date
from datetime import datetime
# ----------------Global variables---------------------------
login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
stock = "SPY"
time = datetime.now().strftime("%H.%M")
time_frame = 'day'
bounds = 'extended'
# if "09.30" <= time <= "16.00":
#     # time_frame = 'week'
#     bounds = 'regular'

# ---------------READ AND WRITE TO TEMP FILE-----------------
def transaction_history(time, msg):
    file_path = "history/transaction_history.txt"
    file = open(file_path, "r")
    txt = ("At " + str(time) + ": " + str(msg) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def clear_record(tmp_file):
    time = datetime.now().strftime("%H.%M")
    if time >= "16.00":
        print("\n!!!IT IS NOW 4:00pm TEMP DATA IS BEING DELETED!!!\n")
        open(tmp_file, 'w').close()
        file_path = tmp_file
        file = open(file_path, "r")
        txt = ("DontDelete" + "\n")
        readFile = file.readlines()
        readFile.insert(1, txt)
        file.close()
        file = open(file_path, "w")
        file = open(file_path, "w")
        file.writelines(readFile)
        file.close()

def read_record_float(indicator):
    data = "history/"+ indicator +"/temp.txt"
    data = [line.rstrip('\n') for line in open(data)]
    data.remove(data[0])
    result = [str(i) for i in data]
    return result[:5]

def read_record_str():
    data = "history/temp.txt"
    data = [line.rstrip('\n') for line in open(data)]
    data.remove(data[0])
    result = [str(i) for i in data]
    return result[:5]

def print_to_temp(tmp_file, n):
    file_path = tmp_file
    file = open(file_path, "r")
    txt = (str(n) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def count_lines_in_temp(indicator):
    tmp_file = "history/"+ indicator +"/temp.txt"
    count = 0
    with open(tmp_file, 'r') as f:
        for line in f:
            count += 1
    return count

def count_lines_in_temp_str():
    tmp_file = "history/temp.txt"
    count = 0
    with open(tmp_file, 'r') as f:
        for line in f:
            count += 1
    return count

# -------------------------------------------------------------

def loopStockInfo(index, stock_data):
    info = [sub[index] for sub in stock_data]
    info = [i for i in info]
    return info

def volume_now():
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [int(i) for i in volume]
    return sum(result[-1:])

def volume_avg():
    volume = 'volume'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    volume = loopStockInfo(volume, stock_data)
    result = [float(i) for i in volume]
    return mean(result[-8:])

def closing_price_n_days(n):
    close_p = 'close_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    return close_p[-n:]

def high_price_n_days(n):
    close_p = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    return close_p[-n:]

def low_price_n_days(n):
    close_p = 'low_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    close_p = loopStockInfo(close_p, stock_data)
    return close_p[-n:]

def close_price_n_with_current_price(n):
    close_p = closing_price_n_days(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    result = [float(i) for i in close_p][-n:]
    return result

def current_price():
    current_stock_price = r.get_latest_price(stock)
    return current_stock_price[0]

def current_high_Price(n=1):
    price = 'high_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    price = loopStockInfo(price, stock_data)
    price = [float(i) for i in price]
    return sum(price[-n:])

def current_low_Price(n=1):
    price = 'low_price'
    stock_data = r.get_historicals(stock, span=time_frame, bounds=bounds)
    price = loopStockInfo(price, stock_data)
    price = [float(i) for i in price]
    return sum(price[-n:])

def ma(n):
    x = [float(i) for i in closing_price_n_days(5)]
    cumsum = numpy.cumsum(numpy.insert(x, 0, 0))
    return sum((cumsum[n:] - cumsum[:-n]) / float(n))

def sma_n(n):
    close_p = closing_price_n_days(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    average = mean(close_p)
    return round(average, 2)

def sma_5(n = 5):
    close_p = closing_price_n_days(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    average = mean(close_p)
    return round(average, 2)

def sma_20(n=20):
    close_p = closing_price_n_days(n)
    current_stock_price = list(current_price().split(" "))
    for i in range(len(current_stock_price)):
        close_p.insert(i + n, current_stock_price[i])
    close_p = [float(i) for i in close_p]
    close_p = mean(close_p)
    return round(close_p, 2)

def ma(n):
    x = [float(i) for i in closing_price_n_days(n)]
    cumsum = numpy.cumsum(numpy.insert(x, 0, 0))
    return sum((cumsum[n:] - cumsum[:-n]) / float(n))

def ema_n(n):
    s, p, a = float((2 / (n + 1))), float(current_price()), sma_n(n)
    r = (p * s) + a * (1-s)
    r = s * p + (1 - s) * a
    r = s * p + (1 - s) * r
    return round(r, 2)

def ema_5(n=5):
    smooth = float((2 / (n + 1)))
    ema_calc = (float(current_price()) * smooth) + sma_5() * (1-smooth)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * sma_5()
    ema_calc = round(ema_calc, 2)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * ema_calc
    return round(ema_calc, 2)

def ema_20(n=20):
    smooth = float((2 / (n + 1)))
    ema_calc = (float(current_price()) * smooth) + sma_20() * (1-smooth)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * sma_20()
    ema_calc = round(ema_calc, 2)
    ema_calc = smooth * float(current_price()) + (1 - smooth) * ema_calc
    return round(ema_calc, 2)

def rsiFunc(n):
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
    rsi1 = round(rsi[0], 2)

    prices = [float(i) for i in closing_price_n_days(n)]
    deltas = np.diff(prices)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100. / (1. + rs)
    for i in range(n, len(prices)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n
        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)
    rsi = rsi.tolist()
    rsi = [float(i) for i in rsi]
    rsi2 = round(rsi[0], 2)
    rsi_ave = ((rsi1 + rsi2) / 2)
    stock_price = float(current_price())
    x = sma_n(5)
    if 0 < rsi_ave < 45:
        result = rsi_ave + 5
    elif 45 < rsi_ave < 55 and x > stock_price:
        result = rsi_ave + 5
    elif 45 < rsi_ave < 55 and x < stock_price:
        result = rsi_ave - 5
    elif 55 < rsi_ave < 100:
        result = rsi_ave - 5
    return rsi1

def rsi_output(n):
    rsi = rsiFunc(n)
    stock_price = float(current_price())
    ema = sma_n(n)
    if 0 < rsi < 15:
        result = "Buy"
    elif 15 < rsi < 70 and stock_price < ema:
        result = "Going down"
    elif 30 < rsi < 75 and stock_price > ema:
        result = "Going up"
    elif 75 < rsi < 100:
        result = "Sell"
    return result

def price_is(n):
    stock_price = float(current_price())
    x = sma_n(n)
    ind = " SMA "
    if stock_price > x:
        result = "above" + ind + str(n)
    elif stock_price < x:
        result = "below" + ind + str(n)
    else:
        result = "equal to" + ind + str(n)
    return "Price is: " + result

def up_or_down(indicator = "ema"):
    stock_price = float(current_price())
    if count_lines_in_temp(indicator) < 6:
        result = "Need data, try again..."
    else:
        x = " SMA "
        r = read_record_float(indicator)
        val_i, val_ii, val_iii, val_iv, val_v = r[0], r[1], r[2], r[3], r[4]
        if val_ii < val_i > val_iii and val_iv < val_iii > val_v:
            result = "Last 5"+x+"are UP"
        elif val_ii < val_iii > val_i and val_iv < val_v > val_iii:
            result = "Last 5"+x+"are DOWN"
        elif val_i == val_ii == val_iii and float(val_i) > stock_price:
            result = "Plateau ^^ ^^ ^^"
        elif val_i == val_ii == val_iii and float(val_i) < stock_price:
            result = "Valley __ __ __"
        elif val_i > val_ii:
            result = "Upward reversal at " + str(stock_price)
        elif val_i < val_ii:
            result = "Downward reversal at " + str(stock_price)
        else:
            result = "not sure at " + str(stock_price)
    return "CONDIT: " + result

def primary_action():
    if count_lines_in_temp_str() > 2:
        val_i, val_ii = read_record_str()[0], read_record_str()[1]
        if count_lines_in_temp_str() == 1:
            result = "Try again. No Data."
        elif val_i == val_ii:
            result = "hold"
        else:
            result = str(val_i)
    else:
        result = "Try again. No Data."
    return result

def output():
    stock_price = float(current_price())
    n = 12
    ema5 = ema_5()
    ema20 = ema_20()
    eman = ema_n(n)
    time = datetime.now().strftime("%H.%M")
    if "09.30" <= time <= "16.00":
        if isclose(ema_5(), ema_20(), abs_tol=1e-2) == True:
            result = "cross"
        if ema5 == ema20 or ema5 == eman or ema20 == eman and stock_price > eman:
            result = "buy " + stock
        elif ema5 == ema20 or ema5 == eman or ema20 == eman and stock_price < eman:
            result = "sell " + stock
        elif current_high_Price() < eman:
            result = "Potential sell " + stock
        elif current_low_Price() > eman:
            result = "Potential buy " + stock
        elif current_low_Price() < eman < current_high_Price():
            result = "Straddle"
        else:
            result = "hold"
    else:
        result = "None - Market Closed"
    transaction_history(time, result + " " + rsi_output(10) + " " + str(rsiFunc(10)))
    return "ACTION: " + result

def print_values(indicator = "ema"):
    tmp_file = "history/" + indicator + "/temp.txt"
    r = sma_n(5)
    print_to_temp(tmp_file, r)
    tmp_file = "history/temp.txt"
    r = rsi_output(10)
    print_to_temp(tmp_file, r)


# ----------------------DATA-----------------------------------
print("+----------INFORMATION---------+")
print("|" + " TIME: " + time + ", STOCK: " + stock)
# print("|" + " PRICE: " + str(float(current_price())))
# print("|" + " RSI " + str(rsiFunc(10)))
print("|" + " EMA 5 " + str(ema_5()))
print("|" + " SMA 5 " + str(sma_5()))
print("|" + " SMA 20 " + str(sma_n(20)))
# print("|" + " EMA 12 " + str(ema_n(12)))
print("|" + " MA 20 " + str(ma(5)))

time = datetime.now().strftime("%H.%M")
if "09.00" <= time <= "16.30":
    print_values()
    print("+------------PRIMARY-----------+")
    print("| " + price_is(20))
    print("| " + "RSI is: " + str(rsiFunc(10)))
    print("| " + "Action: " + primary_action())
    print("+-----------SECONDARY----------+")
    print("| " + up_or_down())
    print("| " + output())
else:
    print("| " + "WAIT: Pre-Market not opened")

print("+------------------------------+")
# -------------------------------------------------------------
