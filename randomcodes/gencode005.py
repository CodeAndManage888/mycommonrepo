import requests

# define the URLs of the two grocery websites
url1 = 'https://puregold.com.ph/pgcatalog/category/view/category/BABY%20CARE'
url2 = 'https://puregold.com.ph/pgcatalog/category/view/category/BABY%20CARE'

# retrieve the price data from the first website
response = requests.get(url1)
data1 = response.json()

# retrieve the price data from the second website
response = requests.get(url2)
data2 = response.json()

# extract the prices for a specific product from the data
product = 'BABY DOVE BAR SOAP SENSITIVE MOISTURE 90G'
price1 = data1[product]['price']
price2 = data2[product]['price']

# compare the prices and print the result
if price1 < price2:
    print(f'{product} are cheaper at grocery website 1 ({price1} vs. {price2})')
elif price1 > price2:
    print(f'{product} are cheaper at grocery website 2 ({price2} vs. {price1})')
else:
    print(f'{product} are the same price at both websites ({price1})')

# This program retrieves the price data for a specific product (in this case, bananas) from two different grocery websites and compares the prices. It then prints a message indicating which website has the lower price for the product, or if the prices are the same at both websites.

# Of course, this is just a simple example, and you may need to modify the code to fit the specific needs of your application. For example, you might want to monitor multiple products, retrieve the data on a regular basis to track price changes, or store the data in a database for further analysis.
