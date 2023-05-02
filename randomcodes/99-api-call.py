#
#-------------------------------------------------------------------
#
from bs4 import BeautifulSoup
import requests
input_site = "https://www.google.com"
response = requests.get(input_site)
print(response.status_code)
print(response.content)
#-------------------------------------------------------------------
#
