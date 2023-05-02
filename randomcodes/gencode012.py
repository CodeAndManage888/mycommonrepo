import requests
import csv
import time

# Set the base URL for the API endpoint
base_url = "https://api.exchangerate-api.com/v4/latest/USD"

# Set the filename for the CSV file
filename = "exchange_rates.csv"

# Clean variables
rowcount = 0

while True:
    # Make a request to the API endpoint
    response = requests	.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the exchange rate data from the response
        data = response.json()
        exchange_rate = data['rates']['PHP']

        # Write the exchange rate to the CSV file
        with open(filename, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([time.ctime(), exchange_rate])
            rowcount = rowcount + 1

    # Wait 5 minutes before making the next request
    time.sleep(30)
    if rowcount == 10:
        break
print('Max rows written to CSV file')
        
