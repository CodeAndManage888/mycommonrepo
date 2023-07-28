from bs4 import BeautifulSoup
import csv

# Replace 'path/to/offline_table.html' with the actual path to your HTML file
html_file_path = '/home/pi/Desktop/localrepo/mycommonrepo/myproject/infile/Lotto Resuts-2013.html'

# Read the contents of the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
content = soup.get_text()

# get the target portion of the page
position1 = content.find("LOTTO GAME")
position2 = content.find("85,745,952.000")
if position1 != -1:
    start = max(0, position1)
    end = position2 + len("85,745,952.000")
portion = content[start:end]
lines = portion.split("\n")

file_path = "/home/pi/Desktop/localrepo/mycommonrepo/myproject/outfile/historical_data.csv"
with open(file_path, "w") as file_handle:
    # clean unnecessary lines in the file
    for line in lines:
        if line != "" and line != "		" and line != "/td>":
            print(line, file=file_handle)

file_handle.close()
                