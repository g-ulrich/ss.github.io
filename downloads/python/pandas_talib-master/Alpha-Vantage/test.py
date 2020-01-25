from statistics import mean

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd

API_KEY = "T7A5GNL10H4G5G0H"
INT = '5min'
STOCK = 'SPY'
PERIOD = 20
TYPE = 'close'
# ts = TimeSeries(key=API_KEY, output_format='pandas')
# data, meta_data = ts.get_intraday(STOCK, interval=INT, outputsize='full')
def ti():
    return TechIndicators(key=API_KEY, output_format='pandas')

def rsi():
    data, meta_data = ti().get_rsi(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return sum(data['RSI'].values.tolist()[-1:])
print("-------------------------------")
print(rsi())
print("-------------------------------")
print("-------------------------------")
print(rsi())
print("-------------------------------")