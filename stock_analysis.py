import pandas as pd

data = {
    "Stock": ["AAPL", "GOOG", "TSLA", "AMZN"],
    "Price": [150, 120, 200, 130]
}

df = pd.DataFrame(data)

print(df)
print("Average:", df["Price"].mean())
