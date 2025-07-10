import numpy as np

def check_growth(df):
    # Use closing prices
    close_prices = df['종가']
    return close_prices.iloc[-1] > close_prices.iloc[0]

def filter_by_per_and_net_worth(df, per_min=5, per_max=10, net_worth_target=1e12, tolerance=0.0005):
    per_cond = (df['PER'] >= per_min) & (df['PER'] <= per_max)
    net_cond = (df['시가총액'] >= net_worth_target * (1 - tolerance)) & (df['시가총액'] <= net_worth_target * (1 + tolerance))
    return df[per_cond & net_cond]

