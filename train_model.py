import yfinance as yf
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

print("Downloading stock data...")

stocks = [
    "AAPL","MSFT","GOOGL","META","NVDA","AMD","TSLA",
    "JPM","BAC","GS",
    "HDFCBANK.NS","ICICIBANK.NS","AXISBANK.NS","SBIN.NS",
    "JNJ","PFE","MRK",
    "SUNPHARMA.NS","DRREDDY.NS",
    "PG","KO","PEP",
    "ITC.NS","HINDUNILVR.NS",
    "XOM","CVX",
    "RELIANCE.NS","ONGC.NS",
    "BHARTIARTL.NS",
    "TCS.NS","INFY.NS","WIPRO.NS"
]

all_data = []

for stock in stocks:

    try:

        print(f"Downloading {stock}...")

        df = yf.download(
            stock,
            start="2019-01-01",
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            continue

        # Fix multi-index columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df["MA20"] = df["Close"].rolling(20).mean()
        df["MA50"] = df["Close"].rolling(50).mean()

        df["Tomorrow"] = df["Close"].shift(-1)

        df = df.dropna()

        df = df[
            [
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "MA20",
                "MA50",
                "Tomorrow"
            ]
        ]

        all_data.append(df)

    except Exception as e:
        print(stock, e)

df = pd.concat(all_data, ignore_index=True)

X = df[
    [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "MA20",
        "MA50"
    ]
]

y = df["Tomorrow"]

print("X shape =", X.shape)

model = RandomForestRegressor(
    n_estimators=50,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

model.fit(X, y)

print("Model features =", model.n_features_in_)

joblib.dump(model, "model.pkl")

print("Model saved successfully!")