import requests
from bs4 import BeautifulSoup

# define the URL of the web page
url = 'https://www.lottopcso.com/'

# retrieve the HTML content of the web page
response = requests.get(url)
html_content = response.text

# parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# find the table element
table = soup.find('table')

# extract the rows from the table
rows = table.find_all('tr')

# extract the data from the rows
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# print the data
print(data)

# This program uses the requests library to retrieve the HTML content of a web page and the BeautifulSoup 
# library to parse the HTML and find the table element. It then extracts the rows from the table and the 
# data from the rows, and stores the data in a list. Finally, it prints the list to the console.

# Keep in mind that this is just a simple example, and you may need to modify the code to fit the 
# specific needs of your application. For example, you might want to extract the data from specific 
# columns or rows, or process the data in some way before storing it.

# Adding a comment to see the difference in git process.
