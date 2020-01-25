from pandas_datareader.data import get_quote_yahoo
import robin_stocks as r

stock='AAPL'

def current_price():
    result = float(get_quote_yahoo(stock)['price'][0])
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



print(current_price())