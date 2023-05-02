import numpy as np
import matplotlib.pyplot as plt
import requests

# define the time period
period = 30

# define the currency pair
currency_pair = 'USD'

# retrieve the exchange rate data from the European Central Bank's website
url = f'https://api.exchangeratesapi.io/history?start_at=2022-01-01&end_at=2022-01-31&base=EUR&symbols={currency_pair}'
response = requests.get(url)
data = response.json()

# extract the high, low, and close prices from the exchange rate data
high = np.array([day_data['rates00'][currency_pair]['high'] for day_data in data['rates00'].values()])
low = np.array([day_data['rates01'][currency_pair]['low'] for day_data in data['rates01'].values()])
close = np.array([day_data['rates02'][currency_pair]['close'] for day_data in data['rates02'].values()])

# calculate the support and resistance levels
support = low[-period:].min()
resistance = high[-period:].max()

# plot the price action
plt.plot(high, 'r')
plt.plot(low, 'g')
plt.plot(close, 'b')

# plot the support and resistance levels
plt.hlines(support, 0, len(high), 'k', linestyles='dashed')
plt.hlines(resistance, 0, len(high), 'k', linestyles='dashed')

# show the plot
plt.show()

#This program retrieves the exchange rate data for the USD/EUR currency pair for the month of January 2022 from the European Central Bank's website, extracts the high, low, and close prices, and calculates and plots the support and resistance levels using the same method as in the previous example.
