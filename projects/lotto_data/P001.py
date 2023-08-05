from bs4 import BeautifulSoup
import csv
from datetime import datetime

def convert_date_format(date_str):
    # Convert the input date string to a datetime object
    date_object = datetime.strptime(date_str, "%m/%d/%Y")

    # Format the datetime object as "Month Day, Year"
    formatted_date = date_object.strftime("%B %d, %Y")

    return formatted_date

# Replace 'path/to/offline_table.html' with the actual path to your HTML file
html_file_path = '/home/pi/Desktop/localrepo/mycommonrepo/projects/lotto_data/infile/Lotto Resuts-2013.html'

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

file_path = "/home/pi/Desktop/localrepo/mycommonrepo/projects/lotto_data/outfile/raw_hist_data.txt"
clean_file_path = "/home/pi/Desktop/localrepo/mycommonrepo/projects/lotto_data/outfile/final_data.txt"
with open(file_path, "w") as file_handle:
    # clean unnecessary lines in the file
    for line in lines:
        if line != "" and line != "		" and line != "/td>":
            print(line, file=file_handle)

file_handle.close()

lotto_list = ["Superlotto 6/49", "Lotto 6/42", "Megalotto 6/45","Grand Lotto 6/55","Ultra Lotto 6/58"]
with open(file_path, "r") as file_record:
    with open(clean_file_path, "w") as file_out:
        recorddata = file_record.readlines()
        for i in range(1, len(recorddata), 2):
            rec1 = recorddata[i].strip()
            rec2 = recorddata[i + 1].strip()
            for items in lotto_list: 
                if items in rec1:
                    clean1 = rec1.replace("=","") + rec2
                    pos1 = clean1.find("/")
                    pos2 = clean1.find("-")
                    detail1 = clean1[pos1 - 1:pos1 + 3]
                    detail2 = clean1[pos2 - 2:pos2 + 15]
                    tmpdtl = clean1[pos2 + 15:pos2 + 25]
                    chkidx1 = tmpdtl.find("/")
                    if chkidx1 == 1:
                        for chkidx2, char in enumerate(tmpdtl):
                            if char == "/" and chkidx2 == 4:
                                detail3 = convert_date_format(clean1[pos2 + 15:pos2 + 24])
                                pos3 = pos2 + 24
                            elif char == "/" and chkidx2 == 3:
                                detail3 = convert_date_format(clean1[pos2 + 15:pos2 + 23])
                                pos3 = pos2 + 23
                    else:
                        for chkidx2, char in enumerate(tmpdtl):
                            if char == "/" and chkidx2 == 5:
                                detail3 = convert_date_format(tmpdtl)
                                pos3 = pos2 + 25
                            elif char == "/" and chkidx2 == 4:
                                detail3 = convert_date_format(clean1[pos2 + 15:pos2 + 24])
                                pos3 = pos2 + 24
                    detail4 = clean1[pos3:len(clean1) - 1]
                    detail5 = clean1[len(clean1) - 1:]
                    outrec = "{:>5} ; {:>20} ; {:>20} ; {:>20} ; {:>5}".format(detail1, detail3, detail2, detail4, detail5)
                    print(outrec, file=file_out)
file_record.close()
file_out.close()
                