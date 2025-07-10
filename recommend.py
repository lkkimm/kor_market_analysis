from src.fetch_data import get_company_list, get_price_history, get_fundamentals
from src.analyze import check_growth, filter_by_per_and_net_worth

def recommend():
    tickers = get_company_list()
    recommendations = []

    for ticker in tickers:
        try:
            f_data = get_fundamentals(ticker)
            price_data = get_price_history(ticker)
            if check_growth(price_data):
                f_data = f_data.to_frame().T
                filtered = filter_by_per_and_net_worth(f_data)
                if not filtered.empty:
                    recommendations.append((ticker, filtered))
        except Exception as e:
            continue

    return recommendations

