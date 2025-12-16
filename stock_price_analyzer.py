import numpy as np
import matplotlib.pyplot as plt

#  Load Dataset
data = np.genfromtxt(
    "data/AAPL.csv",
    delimiter=",",
    skip_header=1,
    usecols=(1, 2, 3, 4, 5)
)

open_p = data[:, 0]
high_p = data[:, 1]
low_p = data[:, 2]
close_p = data[:, 3]
volume = data[:, 4]

# Close Price Trend
plt.figure()
plt.plot(close_p)
plt.title("Stock Close Price Trend")
plt.xlabel("Days")
plt.ylabel("Close Price")
plt.show()

#  Daily Returns
daily_returns = np.diff(close_p) / close_p[:-1]

plt.figure()
plt.plot(daily_returns)
plt.title("Daily Returns")
plt.xlabel("Days")
plt.ylabel("Return")
plt.show()

#  Average Return & Volatility
average_return = np.mean(daily_returns)
volatility = np.std(daily_returns)

print("Average Return:", average_return)
print("Volatility:", volatility)

plt.figure()
plt.hist(daily_returns, bins=50)
plt.title("Daily Returns Distribution")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.show()

#  Best & Worst Trading Day
best_day = np.argmax(daily_returns)
worst_day = np.argmin(daily_returns)

print("Best Day Return:", daily_returns[best_day])
print("Worst Day Return:", daily_returns[worst_day])

#  Moving Average
def moving_average(data, window):
    return np.convolve(data, np.ones(window)/window, mode="valid")

ma_5 = moving_average(close_p, 5)
ma_20 = moving_average(close_p, 20)

plt.figure()
plt.plot(close_p, label="Close Price")
plt.plot(ma_5, label="5-Day MA")
plt.plot(ma_20, label="20-Day MA")
plt.legend()
plt.title("Moving Average Analysis")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()

#  High-Risk Days
risk_threshold = 0.03
high_risk_days = np.where(np.abs(daily_returns) > risk_threshold)

plt.figure()
plt.plot(daily_returns, label="Daily Returns")
plt.scatter(high_risk_days, daily_returns[high_risk_days])
plt.legend()
plt.title("High Risk Trading Days")
plt.xlabel("Days")
plt.ylabel("Return")
plt.show()

# Cumulative Returns
cumulative_returns = np.cumsum(daily_returns)

plt.figure()
plt.plot(cumulative_returns)
plt.title("Cumulative Returns Over Time")
plt.xlabel("Days")
plt.ylabel("Cumulative Return")
plt.show()
