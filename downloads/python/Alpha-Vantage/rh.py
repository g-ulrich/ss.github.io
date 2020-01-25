from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import robin_stocks as r
import numpy as np
from statistics import mean
from datetime import date
from datetime import datetime

login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
TEMP_FILE = 'tmp_files/temp.txt'
TEMP_FILE_OUTPUT = "tmp_files/output.txt"
TRANSACTION_HISTORY = "transactions/history.json"
# other examples of reverse etfs [JNUG, JDST], [TQQQ, SQQQ],
PRIMARY_STOCK = 'JNUG'
SECONDARY_STOCK = 'JDST'

# gabe.bob.ulrich@gmail.com
API_KEY = "T7A5GNL10H4G5G0H"
# gabeustheterminator@gmail.com
API_KEY_2 = "X0I7PRAVQWLKO1R0"
# here4you@cheerful.com
API_KEY_3 = "AWHXTADVQ1C7G1YP"
# gabe.corrinne@yahoo.com
API_KEY_4 = "74804S40FLN6LH82"
# bibleverses@mail.com
API_KEY_5 = "ZC4QOYFRZLS9MT7G"
# gabriel.ulrich@aol.com
API_KEY_6 = "2V6KNRL4NLVIE8CV"
STOCK = 'SPY'
INT = '5min'
TYPE = 'close'

def ti(n):
    if n == 0:
        result = TechIndicators(key=API_KEY, output_format='pandas')
    elif n == 1:
        result = TechIndicators(key=API_KEY_2, output_format='pandas')
    elif n == 2:
        result = TechIndicators(key=API_KEY_3, output_format='pandas')
    elif n == 3:
        result = TechIndicators(key=API_KEY_4, output_format='pandas')
    elif n == 4:
        result = TechIndicators(key=API_KEY_5, output_format='pandas')
    elif n == 5:
        result = TechIndicators(key=API_KEY_6, output_format='pandas')
    else:
        result = TechIndicators(key=API_KEY, output_format='pandas')
    return result


def macd_h_m_s(x=2):
    hist, macd, signal = 'MACD_Hist', 'MACD', 'MACD_Signal'
    data, meta_data = ti(x).get_macd(symbol=STOCK, interval=INT, series_type=TYPE, fastperiod=12, slowperiod=26,
                                     signalperiod=10)
    return [round(float(data[hist].values[0]), 2), round(float(data[macd].values[0]), 2),
            round(float(data[signal].values[0]), 2)]


def stochastic(x=5):
    k, d = 'FastK', 'FastD'
    data, meta_data = ti(x).get_stochf(STOCK, interval=INT, fastkperiod=10, fastdperiod=2, fastdmatype=3)
    # return mean([round(float(data[k].values[0]), 2), round(float(data[d].values[0]), 2)])
    return round(float(data[k].values[0]), 2)


# -----------------------------------ADDITIONS-----------------------------------

def print_to_history(buy_or_sell, stock, time, shares, pps, total):
    file = open(TRANSACTION_HISTORY, "r")
    txt = ('"'+buy_or_sell+'":'+'\n'
           + '   {'+'\n'
           + '      "stock":' + ' ' + '"' + stock + '",'+'\n'
           + '      "time":' + ' ' + '"' + time + '",'+'\n'
           + '      "num_of_shares":' + ' ' + '"' + shares + '",'+'\n'
           + '      "price_per_share":' + ' ' + '"' + pps + '",'+'\n'
           + '      "total_cost":' + ' ' + '"' + total + '"' + '\n'
           + '   },' + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TRANSACTION_HISTORY, "w")
    file.writelines(readFile)
    file.close()


# "buy":
#   {
#     "stock": "TQQQ",
#     "time": "13.00",
#     "shares": "2",
#     "pps": "29.31",
#     "total": "50.61"
#   }

def buy_or_sell(input):
    if input == "sell":
        result ="sell"
        # print_to_history(stock, time, shares, pps, total)
        #                           symbol, quantity,
    elif input == "buy":
        result = "sell"


# execute = r.orders.order_sell_market('TQQQ', 2, timeInForce='gfd', extendedHours='false')
# execute = r.orders.order_sell_limit('TQQQ', 2, current_price()+.02, timeInForce='gtc')


# -----------------------------------ROBINHOOD-----------------------------------
def options_info():
    return r.options.find_options_for_list_of_stocks_by_expiration_date(STOCK, '2020-01-17', optionType='both', info=None)

def current_price():
    current_stock_price = r.get_latest_price(PRIMARY_STOCK)
    return current_stock_price[0]

def loopStockInfo(index, stock_data):
    data = [sub[index] for sub in stock_data]
    return [float(i) for i in data]

def closing_price_n_days():
    prices = 'close_price'
    stock_data = r.get_historicals(PRIMARY_STOCK, span='year', bounds='regular')
    # prices = loopStockInfo(prices, stock_data)
    return loopStockInfo(prices, stock_data)

def account_info():
    buying_power = r.profiles.load_account_profile(info='buying_power')
    type = r.profiles.load_account_profile(info='type')
    return buying_power, type

def equity():
    return r.profiles.load_portfolio_profile(info='equity')

def withdraw_amount():
    return r.profiles.load_portfolio_profile(info='withdrawable_amount')

def current_positions():
    return r.account.get_current_positions(info=None)



# ---------------------------OUTPUTS---------------------------------
# print(options_info())
# print(stochastic())
print(account_info()[1])
print(equity())
print(withdraw_amount())
print(current_positions())
# print_to_history("buy", PRIMARY_STOCK, "9.23", "1", str(current_price()), str(current_price()))



