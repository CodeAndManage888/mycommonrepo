#!/bin/bash
import requests
import os
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
keyword2 = ("6/58", "6/55", "6/49", "6/45", "6/42")
keyword1 = "Lotto GamesWinning NumbersJackpot Prize"

# extract the relevant data from the page
position = content.find(keyword1)
if position != -1:
    start = max(0, position)
    end = position + len(keyword1) + 239
portion = content[start:end]

# extract the details from the cutoff portion
file_path = "/home/pi/Desktop/localrepo/mycommonrepo/myproject/outfile/daily_lotto_result.txt"
ctr1 = 0
while ctr1 < len(keyword2):
    datapos = portion.find(keyword2[ctr1])
    if datapos != -1:
        start = max(0, datapos)
        if ctr1 != 4:
            end = portion.find(keyword2[ctr1 + 1])
        else:
            end = datapos + 50
    datadetail = portion[start:end]
    
# extract per column for storage
    colpos = datadetail.find("-")
    print("{:>5} ; {:>20} ; {:>20} ; {:>20}".format(datadetail[0:4], datadetail[5:colpos - 2], datadetail[colpos - 2:colpos + 15], datadetail[colpos + 15:]))
    file_record = "{:>5} ; {:>20} ; {:>20} ; {:>20}".format(datadetail[0:4], datadetail[5:colpos - 2], datadetail[colpos - 2:colpos + 15], datadetail[colpos + 15:])
    if os.path.exists(file_path):
        record_exists = False
        with open(file_path, "r") as file_handle:
            for line in file_handle:
                if file_record in line:
                    record_exists = True
                    break
        if not record_exists:
            with open(file_path, "a") as file_handle:
                print(file_record, file=file_handle)
    else:
        with open(file_path, "w") as file_handle:
            print(file_record, file=file_handle)
    ctr1 += 1
file_handle.close()

# This program uses the requests library to retrieve the HTML content of a website page and the BeautifulSoup library to parse the HTML and extract the content from the page. It then prints the content to the console.
# Keep in mind that this is just a simple example, and you may need to modify the code to fit the specific needs of your application. For example, you might want to extract specific elements or attributes from the page, or process the content in some way before extracting it.
# <h2 id="lotto-result-history-and-summary">Lotto Result History and Summary</h2>