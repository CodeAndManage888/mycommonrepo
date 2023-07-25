#!/bin/bash
import requests
from bs4 import BeautifulSoup

# define the URL of the website page
url = "https://www.lottopcso.com/"

# retrieve the HTML content of the website page
response = requests.get(url)
html_content = response.text

# parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# extract the content from the page
content = soup.get_text()
keyword3 = ("6/58", "6/55", "6/49", "6/45", "6/42")
keyword1 = "Lotto GamesWinning NumbersJackpot Prize"
keyword2 = "6D"

position = content.find(keyword1)
#position1 = content.find(keyword2)

if position != -1:
    start = max(0, position)
    end = position + len(keyword1) + 240

portion = content[start:end]

print("==========================================================================================================================================================================")
print(portion)
print("==========================================================================================================================================================================")


#lines = content.split("\n")
#for line in lines:
#    if keyword1 in line:
#       print("==========================================================================================================================================================================")
#       print(line)
#       print("==========================================================================================================================================================================")
#       target_content = line
# ----------------------------------------------------------------- Extra Codes ------------------------------------------------------------
# print the content
#print(content)

# write content to a file
#with open('output.txt', 'w', encoding='utf-8') as f:
#    f.write(content)


# This program uses the requests library to retrieve the HTML content of a website page and the BeautifulSoup library to parse the HTML and extract the content from the page. It then prints the content to the console.

# Keep in mind that this is just a simple example, and you may need to modify the code to fit the specific needs of your application. For example, you might want to extract specific elements or attributes from the page, or process the content in some way before extracting it.

# <h2 id="lotto-result-history-and-summary">Lotto Result History and Summary</h2>
