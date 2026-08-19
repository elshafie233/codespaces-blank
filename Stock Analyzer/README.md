# Stock Risk & Return Analyzer

Hey! Welcome to the repo. This is a quick Python script I put together to grab live market data from Yahoo Finance and see how a few heavy-hitters compare on risk and reward. 

Right now, it tracks Apple (AAPL), Microsoft (MSFT), Google (GOOG), and Samsung (005930.KS) starting from the beginning of 2025. 

---

## 🛠️ What You Need to Run It

Just the usual data science stack. Pop open your terminal and run:

```bash
pip install yfinance pandas numpy matplotlib
```

---

## 🚀 How the Logic Works

* **Grabs the data:** It automatically pulls down the 'Close' prices for all four tickers. 
* **Handles international holidays:** Since Samsung trades in South Korea and the others trade in the US, their market holidays don't match. Using `.ffill()` (forward-fill) handles this nicely so a holiday in Seoul doesn't break our US data rows.
* **Math breakdown:** It shifts the raw prices into daily percentage returns, calculates total cumulative profit, and uses standard deviation to see which stock is the most volatile.
* **Visuals:** You get two charts—a busy timeline showing daily return spikes and a clean bar chart comparing overall asset risk.

---

## ⚠️ Sneaky Bugs to Fix in the Code

If you are copying and pasting the raw snippet, keep an eye out for a few quick issues that will trip you up:

1. **The blank image save:** The code calls `plt.show()` right before `plt.savefig()`. Matplotlib clears the active workspace the second `plt.show()` runs, meaning your `standard_deviation.png` will save as a completely blank square. To fix this, just move the save line *above* the show line.
2. **The Sharpe Ratio calculation:** Right now, the script divides the *Total Return* by the *Daily Risk*. Because the timeframes don't match, the resulting numbers will look massive and won't match industry standards. To make it accurate, we need to annualize the math (multiplying the daily risk by the square root of 252 trading days).
3. **Jupyter Notebook syntax:** The line `#matplotlib inline` is great if you are running this in a Jupyter notebook, but if you run it as a regular `.py` script in your terminal, it might throw an error depending on your setup. Keep it commented out unless you are using a notebook!

---

## 💡 Ideas for Twists?
The data uses an end date in August 2026, so it's a solid window of time to analyze. Let me know if you want to tweak this to add a benchmark like the S&P 500 (`^GSPC`) so we can see if these tech stocks are actually beating the market average!
