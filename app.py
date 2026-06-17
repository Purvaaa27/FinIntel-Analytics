from flask import Flask, render_template, request
import yfinance as yf
import joblib
import pandas as pd
import plotly.graph_objects as go
import traceback

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

print("=" * 50)
print("MODEL LOADED")
print("Features expected by model:", model.n_features_in_)
print("=" * 50)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:

        ticker = request.form["ticker"].strip().upper()

        # Currency
        currency = "₹" if ticker.endswith(".NS") else "$"

        # Company Info
        stock = yf.Ticker(ticker)

        try:
            info = stock.info

            company_name = info.get("longName", ticker)
            sector = info.get("sector", "N/A")

            market_cap = info.get("marketCap")
            market_cap = f"{market_cap:,.0f}" if market_cap else "N/A"

            week_high = info.get("fiftyTwoWeekHigh", "N/A")
            week_low = info.get("fiftyTwoWeekLow", "N/A")

        except:
            company_name = ticker
            sector = "N/A"
            market_cap = "N/A"
            week_high = "N/A"
            week_low = "N/A"

        # Historical Data
        history = yf.download(
            ticker,
            period="6mo",
            auto_adjust=True,
            progress=False
        )

        if history.empty:
            return "Invalid Stock Symbol"

        if isinstance(history.columns, pd.MultiIndex):
            history.columns = history.columns.get_level_values(0)

        # Indicators
        history["MA20"] = history["Close"].rolling(20).mean()
        history["MA50"] = history["Close"].rolling(50).mean()

        history.dropna(inplace=True)

        latest = history.tail(1)

        open_price = float(latest["Open"].iloc[0])
        high_price = float(latest["High"].iloc[0])
        low_price = float(latest["Low"].iloc[0])
        close_price = float(latest["Close"].iloc[0])
        volume = int(latest["Volume"].iloc[0])

        ma20 = float(latest["MA20"].iloc[0])
        ma50 = float(latest["MA50"].iloc[0])

        # Features for model
        features = [[
            open_price,
            high_price,
            low_price,
            close_price,
            volume,
            ma20,
            ma50
        ]]

        prediction = float(model.predict(features)[0])

        prediction = max(
            close_price * 0.80,
            min(prediction, close_price * 1.20)
        )

        growth = round(
            ((prediction - close_price) / close_price) * 100,
            2
        )

        # Trend
        if growth > 1:
            signal = "Bullish 📈"
        elif growth < -1:
            signal = "Bearish 📉"
        else:
            signal = "Sideways ➖"

        # Recommendation
        if growth > 3:
            recommendation = "BUY 🟢"
        elif growth < -3:
            recommendation = "SELL 🔴"
        else:
            recommendation = "HOLD 🟡"

        # Confidence
        confidence = round(
            max(
                65,
                min(
                    92,
                    85 - abs(growth) * 2
                )
            ),
            2
        )

        # Chart
        chart_data = history.reset_index()

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=chart_data["Date"],
                y=chart_data["Close"],
                mode="lines",
                name="Close Price"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=chart_data["Date"],
                y=chart_data["MA20"],
                mode="lines",
                name="MA20"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=chart_data["Date"],
                y=chart_data["MA50"],
                mode="lines",
                name="MA50"
            )
        )

        fig.update_layout(
            template="plotly_dark",
            title=f"{ticker} Stock Performance Trend",
            xaxis_title="Date",
            yaxis_title=f"Price ({currency})",
            hovermode="x unified",
            height=650
        )

        graph = fig.to_html(full_html=False)

        disclaimer = (
            "This dashboard is for educational and research purposes only. "
            "Predictions are generated using Machine Learning models and "
            "should not be considered for financial advice."
        )

        return render_template(
            "result.html",
            ticker=ticker,
            currency=currency,
            company_name=company_name,
            sector=sector,
            market_cap=market_cap,
            week_high=week_high,
            week_low=week_low,
            current=round(close_price, 2),
            prediction=round(prediction, 2),
            confidence=confidence,
            signal=signal,
            growth=growth,
            recommendation=recommendation,
            open_price=round(open_price, 2),
            high_price=round(high_price, 2),
            low_price=round(low_price, 2),
            volume=f"{volume:,}",
            disclaimer=disclaimer,
            graph=graph
        )

    except Exception:
        return f"<pre>{traceback.format_exc()}</pre>"


if __name__ == "__main__":
    app.run(debug=True)