import requests
from bs4 import BeautifulSoup

def rsi6():
    url = "http://www.stockta.com/cgi-bin/analysis.pl?symb=SPY&mode=table&table=rsi"
    get = requests.get(url)
    html = get.content
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find_all("td", class_="borderTd")
    div = str(div[0])
    find_phrase = "font"
    phrase = div.find(find_phrase)
    phrase = phrase + len(find_phrase)
    rsi = float(div[phrase+17:phrase+22].strip())
    return(rsi)

def stochastic6():
    url = "https://www.stockta.com/cgi-bin/analysis.pl?symb=SPY&table=stoch&mode=table"
    get = requests.get(url)
    html = get.content
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find_all("td", class_="borderTd")
    div = str(div[0])
    find_phrase = "font"
    phrase = div.find(find_phrase)
    phrase = phrase + len(find_phrase)
    result = float(div[phrase+15:phrase+20].strip())
    return(result)

def fear_and_greed():
    url = "https://money.cnn.com/data/fear-and-greed/"
    get = requests.get(url)
    html = get.content
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find_all(id='needleChart')
    div = str(div[0])
    find_phrase = "Fear &amp; Greed Now: "
    phrase = div.find(find_phrase)
    phrase = phrase + len(find_phrase)
    current_num = int(div[phrase:phrase+3].strip())
    return(current_num)

def combined():
    print("6 MONTH:\n")
    print("Stochastic: \n" + str(stochastic6()))
    print("RSI: \n" + str(rsi6()))
    print("fear and greed: \n" + str(fear_and_greed()))
    if fear_and_greed() >= 85 and rsi6() >= 75 and stochastic6() >= 80:
        result = "Buy SQQQ"
    elif fear_and_greed() <= 15 and rsi6() <= 25 and stochastic6() <= 25:
        result = "Buy TQQQ"
    else:
        result = "nothing"
    return(result)

print("\nPOSITION TO TAKE: " + str(combined()))
