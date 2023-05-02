import requests
from bs4 import BeautifulSoup

# define the URL of the web page
url = 'https://www.lottopcso.com/'

# retrieve the HTML content of the web page
response = requests.get(url)
html_content = response.text

# parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# find the element containing the data you want to extract
element = soup.find(id='wp-block-table tablepress is-style-stripes')

# extract the data from the element
data = element.text

# print the data
print(data)

# This program uses the requests library to retrieve the HTML content of a web page and the BeautifulSoup library to parse the HTML and find the element containing the data you want to extract. It then extracts the data from the element and prints it to the console.

# Keep in mind that this is just a simple example, and you may need to modify the code to fit the specific needs of your application. For example, you might want to use a different method to find the element (such as find_all() or select()) or extract a different attribute from the element (such as href or src).
