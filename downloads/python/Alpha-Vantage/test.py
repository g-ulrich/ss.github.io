from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import robin_stocks as r
import numpy as np
from statistics import mean
from datetime import date
from datetime import datetime
import time

login = r.login('gabe.ulrich@yahoo.com', 'r478dfg61dsQ')
TIME = datetime.now().strftime("%H.%M")
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
TEMP_FILE = 'tmp_files/temp.txt'
TEMP_FILE_OUTPUT = "tmp_files/output.txt"
TRANSACTION_HISTORY = "transactions/history.json"


# ------------------------------ALPHA-VANTAGE-DATA------------------------------------
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


# -----------------------------ALPHA-INDICATORS---------------------------------------

def rsi(x=0, PERIOD=12):
    data, meta_data = ti(x).get_rsi(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return round(float(sum(data['RSI'].values.tolist()[-1:])), 2)


def raw_rsi(n, x=1, PERIOD=12):
    data, meta_data = ti(x).get_rsi(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return data['RSI'].values.tolist()[-n:]


def ema(x=1, PERIOD=5):
    data, meta_data = ti(x).get_ema(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return round(float(sum(data['EMA'].values.tolist()[-1:])), 2)


def bbands_u_m_l(x=2, PERIOD=20):
    u, m, l = 'Real Upper Band', 'Real Middle Band', 'Real Lower Band'
    data, meta_data = ti(x).get_bbands(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return [round(float(data[u].values[0]), 2), round(float(data[m].values[0]), 2), round(float(data[l].values[0]), 2)]


def raw_bbands_u_m_l(x=2, PERIOD=20):
    u, m, l = 'Real Upper Band', 'Real Middle Band', 'Real Lower Band'
    data, meta_data = ti(x).get_bbands(symbol=STOCK, interval=INT, time_period=PERIOD, series_type=TYPE)
    return [round(float(data[u].values[0]), 2), round(float(data[m].values[0]), 2), round(float(data[l].values[0]), 2)]


def macd_h_m_s(x=2):
    hist, macd, signal = 'MACD_Hist', 'MACD', 'MACD_Signal'
    data, meta_data = ti(x).get_macd(symbol=STOCK, interval=INT, series_type=TYPE, fastperiod=14, slowperiod=26,
                                     signalperiod=10)
    return [round(float(data[hist].values[0]), 2), round(float(data[macd].values[0]), 2),
            round(float(data[signal].values[0]), 2)]


def raw_macd_h_m_s(str_input, n, x=3):
    hist, macd, signal = 'MACD_Hist', 'MACD', 'MACD_Signal'
    data, meta_data = ti(x).get_macd(symbol=STOCK, interval=INT, series_type=TYPE, fastperiod=14, slowperiod=26,
                                     signalperiod=10)
    if str_input == "h m s":
        result = [round(float(data[hist].values[0]), 2), round(float(data[macd].values[0]), 2),
                  round(float(data[signal].values[0]), 2)]
    elif str_input == "h":
        result = data[hist].values[:n]
        result = [round(float(i), 2) for i in result]
    elif str_input == "m":
        result = data[macd].values[:n]
        result = [round(float(i), 2) for i in result]
    elif str_input == "s":
        result = data[signal].values[:n]
        result = [round(float(i), 2) for i in result]
    else:
        result = "WRONG INPUT, TRY ('h', 2)"
    return result

def stochastic(x=5):
    k, d = 'FastK', 'FastD'
    data, meta_data = ti(x).get_stochf(STOCK, interval=INT, fastkperiod=29, fastdperiod=2, fastdmatype=3)
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

def clear_record():
    time = datetime.now().strftime("%H.%M")
    if time >= "16.00":
        print("\n!!!IT IS NOW 4:00pm TEMP DATA IS BEING DELETED!!!\n")
        open(TEMP_FILE, 'w').close()
        file, txt = open(TEMP_FILE, "r"), ("DontDelete" + "\n")
        readFile = file.readlines()
        readFile.insert(1, txt)
        file.close()
        file = open(TEMP_FILE, "w")
        file.writelines(readFile)
        file.close()


def read_temp_float():
    data = [line.rstrip('\n') for line in open(TEMP_FILE)]
    data.remove(data[0])
    return [float(i) for i in data]


def read_temp_str():
    data = [line.rstrip('\n') for line in open(TEMP_FILE)]
    data.remove(data[0])
    return [str(i) for i in data]


def print_to_temp(n):
    file, txt = open(TEMP_FILE, "r"), (str(n) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TEMP_FILE, "w")
    file.writelines(readFile)
    file.close()


def print_to_output(n):
    TIME = datetime.now().strftime("%H.%M")
    file, txt = open(TEMP_FILE_OUTPUT, "r"), (TIME + ": " + str(n) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TEMP_FILE_OUTPUT, "w")
    file.writelines(readFile)
    file.close()


def read_output_str():
    data = [line.rstrip('\n') for line in open(TEMP_FILE_OUTPUT)]
    data.remove(data[0])
    return [str(i) for i in data]


def count_lines_in_temp():
    count = 0
    with open(TEMP_FILE, 'r') as f:
        for line in f:
            count += 1
    return count


# -----------------------------------ROBINHOOD-----------------------------------
def current_price():
    current_stock_price = r.get_latest_price(STOCK)
    return current_stock_price[0]

def loopStockInfo(index, stock_data):
    data = [sub[index] for sub in stock_data]
    return [float(i) for i in data]

def closing_price_n_days():
    prices = 'close_price'
    stock_data = r.get_historicals(STOCK, span='year', bounds='regular')
    return loopStockInfo(prices, stock_data)


# ------------------------------------ACTION-------------------------------------

def buy_sell_stochastic():
    result = ""
    s = stochastic()
    if s >= 85.0:
        result = "sell"
    elif s <= 16.0:
        result = "buy"
    else:
        result = "---"
    print_to_output(STOCK + " [" + result + "]")
    print_to_temp(result)
    return result


def buy_sell_macd_and_rsi():
    result = ""
    macd = raw_macd_h_m_s("h", 2)
    m = macd_h_m_s()
    m1, m2 = m[1], m[2]
    r = rsi()
    file = read_temp_str()[0]
    # readFile = read_temp_str()[0]
    # count = count_lines_in_temp()
    # m = macd_h_m_s()
    # m_hist, m_macd, m_signal = m[0], m[1], m[2]
    upper_sell, lower_buy, m_neg, m_pos = macd[0] < macd[1] or r >= 75, macd[0] > macd[1], m1 <= -0.01 and m2 <= -0.01, m1 >= 0.01 and m2 >= 0.01
    up, down, hold, sell, buy = "^^^", "vvv", "---", "sell", "buy"
    if file == buy:
        if macd[0] >= 0.01 or r >= 75:
            if upper_sell:
                result = sell
            else:
                result = up
        else:
            result = hold
    elif file == sell and m_neg:
        if macd[0] <= -0.01 or r <= 20:
            if lower_buy:
                result = buy
            else:
                result = down
        else:
            result = hold
    else:
        if m_neg or m_pos:
            if macd[0] >= 0.02 or r >= 75:
                if upper_sell:
                    result = sell
                else:
                    result = up
            elif macd[0] <= -0.02 or r <= 20:
                if lower_buy:
                    result = buy
                else:
                    result = down
            else:
                result = hold
        else:
            result = hold
    print_to_output(STOCK + " [" + result + "]")
    print_to_temp(result)
    return result

def delineator():
    result = ""
    r = read_temp_str()[:2]
    if r[0] == "buy" or r[0] == "sell":
        if r[0] == r[1]:
            result = ""
        elif r[0] != r[1]:
            result = r[0]
        else:
            result = "Something went wrong with temp file processor."
    else:
        pass
    return result

def main():
    if "09.28" <= TIME <= "16.00":
        for x in range(470):
            if TIME >= "16.00":
                break
            else:
                try:
                    print("~~~~~~~[" + str(x) + "]~~~~~~~")
                    # Processor
                    # result = buy_sell_macd_and_rsi()
                    result = buy_sell_stochastic()
                    print(read_output_str()[0])
                    time.sleep(10)
                    # Delineator
                    if result == "buy" or result == "sell":
                        result = delineator()
                        p = current_price()
                        time.sleep(5)
                        # Read out
                        if result != "":
                            print_to_history(result, STOCK, TIME, "1", str(p), str(p))
                            print("\n\n!!!![At " + TIME + " " + result + " " + STOCK + "]!!!!\n\n")
                        else:
                            pass
                    else:
                        pass
                except:
                    result = "Error!"
            time.sleep(135)
    else:
        result = "Market Closed"
    return result


# ---------------------------EXECUTE---------------------------------
# main()

print(stochastic())