# 📈 FinIntel Analytics

### AI-Powered Financial Market Intelligence Platform

FinIntel Analytics is a Machine Learning-powered stock market analytics platform that provides real-time market insights, stock trend visualization, and AI-driven price forecasting. The platform enables users to analyze stocks from multiple sectors through an interactive fintech-style dashboard.

---

## 🌐 Live Demo

🔗 https://finintel-analytics.onrender.com

## 🚀 Features

### 📊 Real-Time Market Data
- Fetches live and historical stock data using Yahoo Finance.
- Supports both Indian and International stocks.

### 🤖 AI-Based Stock Prediction
- Uses Machine Learning (Random Forest Regression) to predict future stock prices.
- Trained on historical stock market data from multiple sectors.

### 📈 Market Trend Analysis
- Detects Bullish, Bearish, and Sideways market trends.
- Generates Buy, Hold, and Sell recommendations.

### 📉 Interactive Visualization
- Dynamic stock performance charts using Plotly.
- Displays:
  - Closing Price
  - Moving Average 20 (MA20)
  - Moving Average 50 (MA50)

### 🏢 Company Insights
- Company Name
- Sector Information
- Market Capitalization
- 52-Week High & Low
- Daily High & Low
- Trading Volume

### 🎯 Confidence Scoring
- Provides confidence percentage for predictions.
- Helps users understand forecast reliability.

---

## 🏭 Supported Sectors

- Technology
- Banking & Financial Services
- Healthcare & Pharmaceuticals
- FMCG
- Energy & Oil & Gas
- Telecommunications

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Random Forest Regressor

### Data Processing
- Pandas
- NumPy

### Financial Data API
- Yahoo Finance (yfinance)

### Visualization
- Plotly

### Model Storage
- Joblib

### Frontend
- HTML5
- CSS3
- Bootstrap

## 🧠 Machine Learning Workflow

1. Download historical stock market data.
2. Generate technical indicators:
   - MA20 (20-Day Moving Average)
   - MA50 (50-Day Moving Average)
3. Train Random Forest Regression model.
4. Save trained model using Joblib.
5. Predict future stock prices.
6. Generate AI recommendations and market insights.

---

## 📋 Model Features

The model uses the following input features:

- Open Price
- High Price
- Low Price
- Close Price
- Volume
- MA20
- MA50

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Purvaaa27/FinIntel-Analytics.git
cd FinIntel-Analytics
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 🤝 Open for Contributions & Collaboration

FinIntel Analytics is an actively evolving project, and contributions are welcome.

If you have ideas for improvements, new features, performance optimizations, UI enhancements or advanced machine learning models, feel free to contribute.

---



## 👩‍💻 Author

**Purva Pujari**

