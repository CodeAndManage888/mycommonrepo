# Code from social media - YouTube
# Browser History Extract | Status: Working
# How to Use: 
# a. Ensure the source and destination path are correct and files are 
#    available. Execute the code using IDE or terminal.
# --------------------------
import os
import sqlite3
import shutil

#------------ copy database ----------
source_file = '/home/pi/.config/chromium/Default/History'
destination_file = '/home/pi/.config/chromium/Default/History_Extract'
shutil.copy(source_file, destination_file)

#------------ connect and query the database ----------
con = sqlite3.connect('/home/pi/.config/chromium/Default/History_Extract')
cur = con.cursor()
cur.execute("select title, visit_count, last_visit_time from urls")
results = cur.fetchall()

#------------ display the result of the query ----------
for result in results:
	print(result)

#**************************************************************
# Lessons Learned:
# - Q1: I still don't know the complete data structure of the source file.
# - FE01: Create a script that will read the data file on a schedule and 
#   store the formated information ito a storage e.g. database
# ---------------------------------------------------------------------
# Other Use Cases:
# ---------------------------------------------------------------------
# a.) Create a continue watching app to track videos watched from illegal 
#     sites e.g. watch4k.
