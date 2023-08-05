#!/bin/bash
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime

def convert_date_format(date_str):
    # Convert the input date string to a datetime object
    date_object = datetime.strptime(date_str, "%m/%d/%Y")

    # Format the datetime object as "Month Day, Year"
    formatted_date = date_object.strftime("%B %d, %Y")

    return formatted_date

# define the URL of the website page
#url = "https://www.lottopcso.com/"
url = "https://www.pcso.gov.ph/SearchLottoResult.aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# retrieve the HTML content of the website page
response = requests.get(url, headers=headers)
html_content = response.text

# parse the HTML content with Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")

# extract the content from the page
content = soup.get_text()
keyword1 = "LOTTO GAMECOMBINATIONSDRAW DATEJACKPOT (₱)WINNERS"
keyword2 = ("6/58", "6/55", "6/49", "6/45", "6/42")
keyword3 = "Today's National Draws"

#print(content)                                 #uncomment for debugging

# extract the relevant data from the page
position1 = content.find(keyword1)
if position1 != -1:
    start = max(0, position1)
position2 = content.find(keyword3)
if position2 != -1:
    end = max(0, position2)
portion = content[start:end]

#print(portion)                                 #uncomment for debugging

records = portion.split("\n")
records.reverse()

#print(records)                                 #uncomment for debugging

# extract the details from the cutoff portion
file_path = "/home/pi/Desktop/localrepo/mycommonrepo/projects/lotto_data/outfile/daily_lotto_result.txt"
for entry in records:
    ctr1 = 0
    while ctr1 <= len(keyword2) - 1:
        datapos = entry.find(keyword2[ctr1])
        if datapos != -1:
            start = max(0, datapos)
            datadetail = entry[start:]
#            print(datadetail)                                 #uncomment for debugging
            detail1 = datadetail[0:4]                          #lotto game
            tmpdtl = datadetail[21:]
            chkidx1 = tmpdtl.find("/")
            if chkidx1 == 1:
                for chkidx2, char in enumerate(tmpdtl):
                    if char == "/" and chkidx2 == 4:
                        detail2 = convert_date_format(datadetail[21:30])    #formatted data
                        pos1 = 30
                    elif char == "/" and chkidx2 == 3:
                        detail2 = convert_date_format(datadetail[21:29])    #formatted data
                        pos1 = 29
            else:
                for chkidx2, char in enumerate(tmpdtl):
                    if char == "/" and chkidx2 == 5:
                        detail2 = convert_date_format(datadetail[21:31])    #formatted data
                        pos1 = 31
                    elif char == "/" and chkidx2 == 4:
                        detail2 = convert_date_format(datadetail[21:30])    #formatted data
                        pos1 = 30
            detail3 = datadetail[4:21]                                      #winning numbers
            detail4 = datadetail[pos1:len(datadetail)]                      #total prize
            detail5 = datadetail[len(datadetail)-1:]                        #total number of winners
# extract per column for storage
#           print("{:>5} ; {:>20} ; {:>20} ; {:>20} ; {:>5}".format(detail1, detail2, detail3, detail4, detail5))           #uncomment for debugging
            file_record = "{:>5} ; {:>20} ; {:>20} ; {:>20} ; {:>5}".format(detail1, detail2, detail3, detail4, detail5)
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
