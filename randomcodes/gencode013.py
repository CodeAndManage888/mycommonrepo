import requests
import datetime

# Define the URL of the search results page
#url = "https://www.pcso.gov.ph/SearchLottoResult.aspx"
url = "https://www.lottopcso.com/"


# Define the start and end dates for the search
#today = datetime.datetime.now()
#end_date = today.strftime("%Y-%m-%d")
#start_date = (today - datetime.timedelta(days=365)).strftime("%Y-%m-%d")

# Replace the placeholder values in the URL with the start and end dates
#url = url.format(start_date=start_date, end_date=end_date)

# Send a GET request to the URL and store the response
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Extract the search results from the response
    results = response.json()["results"]

    # Loop through the results and print each one
    for result in results:
        print(result)
else:
    # Print an error message if the response was not successful
    print("An error occurred while trying to retrieve the search results.")

        
