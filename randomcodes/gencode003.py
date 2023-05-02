import numpy as np
import matplotlib.pyplot as plt

# define the time period
period = 30

# define the high, low, and close prices
high = np.array([100, 105, 102, 110, 120, 115, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240])
low = np.array([50, 55, 45, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190])
close = np.array([75, 80, 70, 85, 90, 95, 105, 115, 120, 130, 135, 145, 150, 155, 165, 170, 180, 185, 190, 200, 205, 210, 220, 225, 235, 240, 245, 250, 255, 260])

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

#This program calculates the minimum low price over the last 30 time periods as the support level and the maximum high price over the last 30 time periods as the resistance level. It then plots the high, low, and close prices as a line chart and overlays the support and resistance levels as horizontal dashed lines.
