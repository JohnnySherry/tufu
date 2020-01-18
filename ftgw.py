from futu import *
def read():
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    print(quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.WARRANT))
    print(quote_ctx.get_stock_basicinfo(Market.US, SecurityType.STOCK, 'US.AAPL'))
    tp=quote_ctx.get_market_snapshot('HK.00700')
    print(tp)
    quote_ctx.close()

if __name__ == "__main__":
    read()