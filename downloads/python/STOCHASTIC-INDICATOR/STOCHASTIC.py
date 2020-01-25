from alpha_vantage.techindicators import TechIndicators
import robin_stocks as r
import pandas_market_calendars as mcal
import pandas as pd
import ast
from datetime import datetime
import time

USERNAME = 'gabe.ulrich@yahoo.com'
PASSWORD = 'r478dfg61dsQ'
login = r.login(USERNAME, PASSWORD)

DN = datetime.now()
TIME = DN.strftime("%H.%M")
DAY = DN.strftime("%d")
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
STOCK = 'NIO'
INT = '5min'
TYPE = 'close'
TEMP_FILE = 'tmp_files/temp.txt'
TEMP_FILE_OUTPUT = "tmp_files/output.txt"
TRANSACTION_HISTORY = "transactions/history.txt"


def LOGIN_ROBINHOOD():
    r.authentication.login(USERNAME, PASSWORD, expiresIn=86400, scope='internal', by_sms=True, store_session=True)


def LOGOUT_ROBINHOOD():
    r.authentication.logout()


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


def ema(x=1, PERIOD=100):
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


def stochastic_k_d(x=5):
    k, d = 'FastK', 'FastD'
    data, meta_data = ti(x).get_stochf(STOCK, interval=INT, fastkperiod=19, fastdperiod=3, fastdmatype=3)
    return [round(float(data[k].values[0]), 0), round(float(data[d].values[0]), 0)]


# -----------------------------------ADDITIONS-----------------------------------
def print_to_history(buy_or_sell, time, shares, pps, total):
    file = open(TRANSACTION_HISTORY, "r")
    txt = "{'day':'" + DAY + "','signal':'" + buy_or_sell + "','stock':'" + STOCK + "','time':" \
                                                                                    "'" + time + "','shares':'" + shares + "','price':'" + pps + "','total':'" + total + "'},"
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TRANSACTION_HISTORY, "w")
    file.writelines(readFile)
    file.close()


def read_history_str():
    data = [line.rstrip('\n') for line in open(TRANSACTION_HISTORY)]
    data.remove(data[0])
    return [str(i) for i in data]


def count_lines_in_history():
    count = 0
    with open(TRANSACTION_HISTORY, 'r') as f:
        for line in f:
            count += 1
    count = count - 1
    return count


def clear_record(file_path_and_name):
    time_now = datetime.now().strftime("%H.%M")
    if time_now >= "16.00":
        print("!CLEARED! " + file_path_and_name)
        open(file_path_and_name, 'w').close()
        file, txt = open(file_path_and_name, "r"), ("DontDelete" + "\n")
        readFile = file.readlines()
        readFile.insert(1, txt)
        file.close()
        file = open(file_path_and_name, "w")
        file.writelines(readFile)
        file.close()


def clear_records():
    clear_record(TEMP_FILE)
    time.sleep(1)
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    print_to_temp("---")
    clear_record(TEMP_FILE_OUTPUT)
    time.sleep(1)
    print_to_output("[data cleared]")


def read_temp_float():
    data = [line.rstrip('\n') for line in open(TEMP_FILE)]
    data.remove(data[0])
    return [float(i) for i in data]


def read_temp_str():
    data = [line.rstrip('\n') for line in open(TEMP_FILE)]
    data.remove(data[0])
    return [str(i) for i in data]


def print_to_temp(input_string):
    file, txt = open(TEMP_FILE, "r"), (str(input_string) + '\n')
    readFile = file.readlines()
    readFile.insert(1, txt)
    file.close()
    file = open(TEMP_FILE, "w")
    file.writelines(readFile)
    file.close()


def print_to_output(input_string):
    TIME = datetime.now().strftime("%H.%M")
    file, txt = open(TEMP_FILE_OUTPUT, "r"), (TIME + ": " + str(input_string) + '\n')
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


def transaction_history_day_sig_sha_pps_tot():
    day, signal, stock, time, shares, prices, total = "day", "signal", "stock", "time", "shares", "price", "total"
    history = str(read_history_str()).replace('"', '')
    history = ast.literal_eval(history)
    days = loopStockInfo_float(day, history)
    signals = loopStockInfo_str(signal, history)
    shares = loopStockInfo_float(shares, history)
    pps = loopStockInfo_float(prices, history)
    total = loopStockInfo_float(total, history)
    return days, signals, shares, pps, total


def minutes_to_close():
    import datetime
    now = datetime.datetime.now()
    from datetime import datetime
    then = datetime(now.year, now.month, now.day, 16, 3, 00)
    now = datetime.now()
    duration = then - now
    return int(duration.total_seconds() / 60)


def market_open_or_closed():
    import datetime
    now = datetime.datetime.now()
    date, year = str(now.strftime("%Y-%m-%d")), str(now.year)
    market_trading_days = mcal.get_calendar('NYSE').schedule(start_date=date, end_date=year + '-12-29')
    market_open = pd.to_datetime(str(market_trading_days['market_open'].values[0]))
    market_closed = pd.to_datetime(str(market_trading_days['market_close'].values[0]))
    market_open_date = market_open.strftime('%Y-%m-%d')
    # market_open_time = market_open.strftime('%H.%M')
    # market_close_time = market_closed.strftime('%H.%M')
    return market_open_date


def date_now():
    return datetime.now().strftime("%Y-%m-%d")


def time_now():
    return datetime.now().strftime("%H.%M")


# -----------------------------------ROBINHOOD-----------------------------------
def current_price():
    current_stock_price = r.get_latest_price(STOCK)
    return current_stock_price[0]


def current_price_of(symbol):
    current_stock_price = r.get_latest_price(symbol)
    return current_stock_price[0]


def loopStockInfo(index, stock_data):
    data = [sub[index] for sub in stock_data]
    return [float(i) for i in data]


def loopStockInfo_str(index, stock_data):
    data = [sub[index] for sub in stock_data]
    return [str(i) for i in data]


def loopStockInfo_float(index, stock_data):
    data = [sub[index] for sub in stock_data]
    return [float(i) for i in data]


def closing_price_n_days():
    prices = 'close_price'
    stock_data = r.get_historicals(STOCK, span='year', bounds='regular')
    return loopStockInfo(prices, stock_data)


def account_info_pow_type():
    buying_power = r.profiles.load_account_profile(info='buying_power')
    type = r.profiles.load_account_profile(info='type')
    return float(buying_power), type


def portfolio():
    equity = r.profiles.load_portfolio_profile(info='equity')
    withdraw = r.profiles.load_portfolio_profile(info='withdrawable_amount')
    return equity, withdraw


def current_positions_sha_pps_tot():
    positions = r.account.get_current_positions(info=None)
    if positions == [None]:
        result = "0.0", "0.0", "0.0"
    else:
        quantity = r.account.get_current_positions(info='quantity')
        avg_price = r.account.get_current_positions(info='average_buy_price')
        q, ap = float(quantity[0]), float(avg_price[0])
        total = q * ap
        result = str(q), str(ap), str(total)
    return result


def get_portfolio_symbols():
    symbols = []
    holdings_data = r.get_current_positions()
    for item in holdings_data:
        if not item:
            continue
        instrument_data = r.get_instrument_by_url(item.get('instrument'))
        symbol = instrument_data['symbol']
        symbols.append(symbol)
    return symbols[0]

def inflation_or_deflation():
    e, c = ema(), float(current_price())
    if e < c: inflated_deflated = "up"
    elif e > c: inflated_deflated = "down"
    else: inflated_deflated = "nothing"
    return inflated_deflated

# ------------------------------------ACTION-------------------------------------

def market_order(buy_or_sell):
    buying_power, percentage_of_cash, stock_price = account_info_pow_type()[0], .25, float(current_price_of(STOCK))
    cash_to_buy = buying_power * percentage_of_cash
    # shares_to_buy = int(cash_to_buy / stock_price)
    shares_to_buy = 1
    p = current_positions_sha_pps_tot()
    current_shares, avg_price, total_cost = float(p[0]), p[1], p[2]
    if buy_or_sell == "sell":
        # if current_shares >= 1.0:
        r.orders.order_sell_market(STOCK, current_shares, timeInForce='gfd', extendedHours='false')
        # else:
        #     pass
    elif buy_or_sell == "buy":
        r.orders.order_buy_market(STOCK, shares_to_buy, timeInForce='gfd', extendedHours='false')
    else:
        print("Error in market_order() neither buy or sell.")


def buy_sell_stochastic():
    # result = ""
    # s = stochastic_k_d()
    # k, d = float(s[0]), float(s[1])
    # if k >= 85.0 and k == d:
    #     result = "sell"
    # elif k <= 16.0 and k == d:
    #     result = "buy"
    # else:
    #     result = "---"
    # print_to_output(STOCK + " [" + result + "]")
    # print_to_temp(result)
    # return result
    result = ""
    s = stochastic_k_d()
    k, d = float(s[0]), float(s[1])
    if d >= 85.0:
        result = "sell"
    elif d <= 16.0:
        result = "buy"
    else:
        result = "---"
    print_to_output(STOCK + " [" + result + "] " + "[K: " + str(k) + "] [D: " + str(d) + "]")
    print_to_temp(result)
    return result, k, d


def delineator():
    result = ""
    r = read_temp_str()[:7]
    d_or_f = inflation_or_deflation()
    if r[0] == "buy" or r[0] == "sell":
        if d_or_f == "up":
            if r[0] == "sell":
                if r[0] == r[1] and r[1] == r[3] and r[3] == r[5] and r[5] == r[6]:
                    if r[0] != r[7]:
                        result = r[0]
                    else: pass
                else: pass
            elif r[0] == "buy":
                result == r[0]
            else: pass
        elif d_or_f == "down":
            if r[0] == "buy":
                if r[0] == r[1] and r[1] == r[3] and r[3] == r[5] and r[5] == r[6]:
                    if r[0] != r[7]:
                        result = r[0]
                    else:
                        pass
                else:
                    pass
            elif r[0] == "sell":
                result == r[0]
            else:
                pass
        else:
            if r[0] == r[1] and r[1] == r[2]:
                if r[0] != r[3]:
                    result = r[0]
                else: pass
            else: pass
    else: pass
    return result


def biscuit_cooking():
    delay = 144
    offset_loop = ((delay + 6) / 60)
    m = int((minutes_to_close() / offset_loop))
    for x in range(m):
        print("~~~~~~~[" + str(x) + "/" + str(m) + "]~~~~~~~")
        NOW_TIME = datetime.now().strftime("%H.%M")
        # Processor
        try:
            indicator = buy_sell_stochastic()
            result, k, d = indicator[0], indicator[1], indicator[2]
            print(NOW_TIME + " " + STOCK + " [" + result + "]")
            print("[K: " + str(k) + "] [D: " + str(d) + "]")
        except:
            pass
        try:
            p = current_positions_sha_pps_tot()
            current_shares, avg_price, total_cost = float(p[0]), p[1], p[2]
            print("S: " + str(current_shares) + " A_p: $" + str(avg_price))
            # print("Avg Price $" + str(avg_price))
            print(STOCK + " Price: $" + str(current_price()))
        except:
            pass
        if result == "buy" or result == "sell":
            try:
                buy_or_sell = delineator()
                time.sleep(5)
                # ACTION
                if buy_or_sell != "":
                    buying_power, percentage_of_cash, stock_price = account_info_pow_type()[0], .25, float(
                        current_price_of(STOCK))
                    cash_to_buy = buying_power * percentage_of_cash
                    # shares_to_buy = int(cash_to_buy / stock_price)
                    shares_to_buy = 1
                    p = current_positions_sha_pps_tot()
                    current_shares, avg_price, total_cost = float(p[0]), p[1], p[2]
                    if buy_or_sell == "sell":
                        # if current_shares >= 1.0:
                        r.order_sell_market(STOCK, current_shares)
                        # else:
                        #     pass
                    elif buy_or_sell == "buy":
                        r.order_buy_market(STOCK, 1)
                    else:
                        print("Error in market_order() neither buy or sell.")
                    print(STOCK + " " + buy_or_sell + " order success!")
                else:
                    pass
            except:
                pass
        else:
            pass
        time.sleep(delay)


# def main():
#     i = 5
#     while i > 4:
#         date_now = datetime.now().strftime("%Y-%m-%d")
#         market_open_date = market_open_or_closed()
#         if market_open_date == date_now:
#             # LOGIN_ROBINHOOD()
#             time_now = datetime.now().strftime("%H.%M")
#             if "09.30" <= time_now <= "16.00":
#                 while time_now <= "16.00":
#                     print(biscuit_cooking())
#                     time_now = "16.01"
#             elif "16.00" <= "16.01" <= "16.30":
#                 print("MARKET CLOSED")
#                 # LOGOUT_ROBINHOOD()
#                 clear_records()
#                 # 2000 / 60 = 33.3 minutes
#                 time.sleep(2000)
#             else:
#                 pass
#         else:
#             # five_or_zero = datetime.now().strftime("%H.%M")[-1]
#             # if five_or_zero == "5" or five_or_zero == "0":
#             pass

def main():
    if market_open_or_closed() == date_now():
        hr_mm = time_now()
        print(".")
        if hr_mm >= "16.30":
            while hr_mm < "09.28":
                hr_mm = time_now()
                print("..")
        elif "09.30" <= hr_mm <= "16.00":
            while hr_mm <= "16.00":
                print(biscuit_cooking())
                hr_mm = "16.01"
        elif "16.00" <= "16.01" <= "16.30":
            print("MARKET CLOSED")
            # LOGOUT_ROBINHOOD()
            clear_records()
            time.sleep(2000)  # 33.3 min
        else:
            print("...")
            pass


# ---------------------------EXECUTE---------------------------------

main()
