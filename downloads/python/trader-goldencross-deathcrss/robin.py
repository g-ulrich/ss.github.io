import click, json
import robin_stocks as rh

@click.group()
def main():
    print("hello world from main")


@main.command(help="Gets a stock quote from one or more symbols")
@click.argument('symbols', nargs=-1)
def quote(symbols):
    for symbol in symbols:
        print("Getting a stock quote for symbol {}".format(symbol))
    # content = open('config.json').read()
    # config = json.loads(content)
    # print(config)
    # #rh.login(config['username'], config['password'])
    #
    # quotes = rh.get_quotes(symbols)
    # print(quotes)

    #for symbols in symbols:
    #   print("Getting a stock quote for symbol {}".format(symbol))

    @main.command(help='Gets quotes for all stocks in your watchlist')
    def watchlist():
        print("Getting quotes for watchlist")

    if __name__ == '__main__':
        main()