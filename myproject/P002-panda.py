from bs4 import BeautifulSoup
import pandas as pd

# Replace 'path/to/offline_table.html' with the actual path to your HTML file
html_file_path = '/home/pi/Desktop/localrepo/mycommonrepo/myproject/infile/Lotto Resuts-2013.html'

# Read the contents of the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element in the HTML content
# If you know the specific table's ID or class, you can use find() or find_all() accordingly
table = soup.find('table')

# Convert the HTML table to a pandas DataFrame
df = pd.read_html(str(table))[0]

# Now you have the table data in a pandas DataFrame (df) which you can work with
print(df)
