# 📈 Stock Price Numerical Analyzer (NumPy)

A beginner-to-intermediate **data analysis project** that uses **NumPy and Matplotlib** to perform numerical analysis on real stock market data (Apple – AAPL).

This project focuses on understanding **price movement, risk, and trends** using core NumPy concepts without relying on heavy libraries like Pandas.

---

## 🎯 Project Objective

The main objective of this project is to:
- Practice **NumPy array operations** on real-world data
- Perform **financial numerical analysis**
- Visualize trends and risk using **Matplotlib**
- Build a **GitHub-ready project** suitable for internships and placements

---

## 🔍 Features & Analysis Performed

- 📥 Load stock price data from CSV using NumPy
- 📊 Visualize **closing price trend**
- 📉 Calculate **daily returns**
- 📐 Compute **average return** and **volatility**
- 🏆 Identify **best and worst trading days**
- 📈 Perform **moving average analysis** (5-day & 20-day)
- ⚠️ Detect **high-risk trading days** (±3% return)
- 📊 Plot **cumulative returns** over time

---

## 🧠 Concepts Used (NumPy Focus)

- `np.genfromtxt()` – loading CSV data
- Array slicing and indexing
- `np.diff()` – daily price change
- `np.mean()` & `np.std()` – statistics
- `np.argmax()` & `np.argmin()`
- `np.convolve()` – moving average
- `np.where()` – risk detection
- `np.cumsum()` – cumulative returns

---

## 🛠️ Technologies Used

- **Python**
- **NumPy**
- **Matplotlib**
- **Google Colab**

---

## 📂 Project Structure
Stock-Price-Numerical-Analyzer/
│
├── data/
│ └── AAPL.csv # Stock price dataset
│
├── notebooks/
│ └── stock_price_analysis.ipynb # Colab/Jupyter notebook
│
├── src/
│ └── stock_price_analyzer.py # Python script version
│
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

2️⃣ Run Python Script

python src/stock_price_analyzer.py
Or open the notebook:
notebooks/stock_price_analysis.ipynb

📊 Dataset Information

Company: Apple Inc. (AAPL)

Type: Historical stock price data

Columns Used: Open, High, Low, Close, Volume

Source: Yahoo Finance / Kaggle



🎓 Learning Outcomes

After completing this project, I gained:

Strong understanding of NumPy for numerical analysis

Experience working with real financial datasets

Confidence in data visualization

Knowledge of project structuring for GitHub

Practical exposure to risk and return analysis


🚀 Future Improvements

Add Pandas-based version

Save plots automatically to /images

Add command-line arguments

Extend analysis to multiple stocks

Perform correlation & comparison analysis


👨‍💻 Author

Yuvraj Singh Rathore
CSE (AI & ML) Student
Aspiring Data Scientist | Python & NumPy Enthusiast
