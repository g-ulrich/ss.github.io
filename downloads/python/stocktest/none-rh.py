import inline as inline
import matplotlib
from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
import numpy as np
import datetime
from datetime import datetime, timedelta
from pandas_datareader.data import get_quote_yahoo


# -------------------------------------------------
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
# % matplotlib
inline
stock = 'SPY'
start = '1/1/2019'
end = '12/30/2019'

def get_stock(stock = 'SPY', start = '1/1/2019', end = '12/30/2019'):
    result = web.DataReader(stock, 'yahoo', start, end)['Close']
    result = [float(i) for i in result]
    return result

def RSI(series, period):
    delta = series.diff()
    # series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period - 1]] = np.mean(u[:period])  # first value is sum of avg gains
    u = u.drop(u.index[:(period - 1)])
    d[d.index[period - 1]] = np.mean(d[:period])  # first value is sum of avg losses
    d = d.drop(d.index[:(period - 1)])
    rs = pd.stats.moments.ewma(u, com=period - 1, adjust=False) / \
         pd.stats.moments.ewma(d, com=period - 1, adjust=False)
    return 100 - 100 / (1 + rs)


print(RSI(get_stock(), 14))
# print(get_stock())
# df = pd.DataFrame(get_stock(stock = 'SPY', start = '1/1/2019', end = '12/30/2019'))
# df['RSI'] = RSI(df['Close'], 14)
# df.tail()





















stock='SPY'
day = 1
week = 7
month = 30
year = 365

def current_price():
    result = float(get_quote_yahoo(stock)['price'][0])
    print_to_temp(result)
    return(result)

def price_data_float_n(n):
    data = "history/price/price_temp.txt"
    data = [line.rstrip('\n') for line in open(data)]
    data.remove(data[0])
    result = [float(i) for i in data]
    result = result[:n]
    return(result)

def print_to_temp(n):
    file_path = "history/price/price_temp.txt"
    file = open(file_path, "r")
    txt = (str(n) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(file_path, "w")
    file.writelines(readFile)
    file.close()

def date_n_days_ago(n):
    result = datetime.now() - timedelta(days=n)
    return(result)

def todays_date():
    result = datetime.now()
    return (result)

def close_price_n(n):
    result = data.DataReader('SPY', 'yahoo', date_n_days_ago(n), todays_date())['Adj Close']
    result = [float(i) for i in result]
    return(result)

def rsiFunc(n=14):
    prices = price_data_float_n(15)
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



def rsi():
    period = 14
    series = pd.Series(close_price_n(14))
    print(series)
    delta = series.diff().dropna()
    u = delta * 0
    d = u.copy()
    u[delta > 0] = delta[delta > 0]
    d[delta < 0] = -delta[delta < 0]
    u[u.index[period - 1]] = np.mean(u[:period])  # first value is sum of avg gains
    u = u.drop(u.index[:(period - 1)])
    d[d.index[period - 1]] = np.mean(d[:period])  # first value is sum of avg losses
    d = d.drop(d.index[:(period - 1)])
    rs = pd.stats.moments.ewma(u, com=period - 1, adjust=False) / \
         pd.stats.moments.ewma(d, com=period - 1, adjust=False)
    return 100 - 100 / (1 + rs)

# print(rsiFunc())
# print(rsi())