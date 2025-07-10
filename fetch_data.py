from pykrx import stock
import pandas as pd
from datetime import datetime, timedelta

def get_company_list():
    today = datetime.today().strftime("%Y%m%d")
    return stock.get_market_ticker_list(today, market="KOSPI")

def get_fundamentals(ticker):
    today = datetime.today().strftime("%Y%m%d")
    df = stock.get_market_fundamental_by_ticker(today)
    return df.loc[ticker]

def get_price_history(ticker):
    today = datetime.today()
    two_months_ago = today - timedelta(days=60)
    return stock.get_market_ohlcv_by_date(two_months_ago.strftime('%Y%m%d'), today.strftime('%Y%m%d'), ticker)


