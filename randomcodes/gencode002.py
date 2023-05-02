import csv
import requests
from bs4 import BeautifulSoup

# Get the HTML content of the website
url = "https://puregold.com.ph/pgcatalog/category/view/category/BABY%20CARE"
response = requests.get(url)
html = response.text

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Find the product names and prices
products = []
for item in soup.find_all("div", class_="product-item"):
    name = item.find("h2").text
    price = item.find("span", class_="price").text
    products.append((name, price))

# Write the product names and prices to a CSV file
with open("products.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(products)

print("Done!")

#This script uses the requests and Beautiful Soup libraries to send an HTTP request to the website and parse the HTML content. It then uses the find_all and find methods of the Beautiful Soup object to locate the product names and prices in the HTML. Finally, it writes the product names and prices to a CSV file using the csv library.

#To use this script, you will need to replace <url> with the URL of the grocery website you want to scrape. You will also need to have the requests, Beautiful Soup, and csv modules installed. You can install these modules using pip: pip install requests bs4 csv.

#Keep in mind that web scraping can be against the terms of use of some websites, and you should respect the website's terms and policies. Additionally, the structure of the HTML content may change over time, which could cause the script to stop working. You may need to update the script or use a different approach if this happens.
