import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'GOOG', '005930.KS']


raw_data = yf.download(tickers, start='2025-01-01', end='2026-08-18')

df = raw_data['Close']

df = df.ffill().dropna()

df = df.pct_change()

standard_deviation = df.std()
print("Standard Deviation of Daily Returns:")
print(standard_deviation)

Total_Return = (df + 1).prod() - 1
print("\nTotal Return:")
print(Total_Return)

sharp_ratio = Total_Return / standard_deviation
print("\nSharpe Ratio:")
print(sharp_ratio)

#matplotlib inline

plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(df[ticker], label=ticker)
plt.title('Daily Returns of Selected Stocks')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.grid()
plt.show()

bar_chart = standard_deviation.plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Standard Deviation of Daily Returns')
plt.xlabel('Ticker')
plt.ylabel('Standard Deviation')
plt.xticks(rotation=0)
plt.show()  

plt.savefig('standard_deviation.png')
