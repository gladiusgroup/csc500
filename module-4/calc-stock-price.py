stock_prices = [
    {"date": "2023-01-01", "stock": "XYZ Corp", "open": 100, "close": 105},
    {"date": "2023-01-02", "stock": "XYZ Corp", "open": 105, "close": 103},
    {"date": "2023-01-03", "stock": "XYZ Corp", "open": 103, "close": 108},
    # ... more data ...
]

for price in stock_prices:
    percentage_change = ((price["close"] - price["open"]) / price["open"]) * 100
    print(f"{price['date']}: {price['stock']} changed {percentage_change:.2f}%")
