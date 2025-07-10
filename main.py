from src.recommend import recommend

def main():
    results = recommend()
    for ticker, data in results:
        print(f"Ticker: {ticker}")
        print(data)
        print("="*40)

if __name__ == "__main__":
    main()

