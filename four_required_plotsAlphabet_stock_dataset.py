pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("alphabet_stock_data.csv")

# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Select date range
start_date = '2020-01-01'
end_date = '2020-12-31'

# Filter data between two dates
data = df[(df['Date'] >= start_date) &
          (df['Date'] <= end_date)]

# 1. Line plot of stock prices
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'], label='Closing Price')
plt.title('Alphabet Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar plot of trading volume
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Volume'])
plt.title('Alphabet Trading Volume')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Stacked histogram of stock prices
plt.figure(figsize=(10, 5))

plt.hist(
    [data['Open'], data['Close'], data['High'], data['Low']],
    bins=50,
    stacked=True,
    label=['Open', 'Close', 'High', 'Low']
)

plt.title('Stacked Histogram of Stock Prices')
plt.xlabel('Stock Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 4. Scatter plot of trading volume and stock price
plt.figure(figsize=(10, 5))
plt.scatter(data['Volume'], data['Close'])

plt.title('Trading Volume vs Stock Price')
plt.xlabel('Trading Volume')
plt.ylabel('Closing Price')
plt.show()