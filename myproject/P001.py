from bs4 import BeautifulSoup
import csv

# Replace 'path/to/offline_table.html' with the actual path to your HTML file
html_file_path = '/home/pi/Desktop/localrepo/mycommonrepo/myproject/infile/Lotto Resuts.html'

# Read the contents of the HTML file
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
content = soup.get_text()

# Find the table element in the HTML content
# If you know the specific table's ID or class, you can use find() or find_all() accordingly
table = soup.find('table')

# Create a CSV file and write the table data into it
# Replace 'path/to/output_file.csv' with the path where you want to save the CSV file
output_csv_path = '/home/pi/Desktop/localrepo/mycommonrepo/myproject/outfile/historical_data.csv'

with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Extract data from each row of the table and write it to the CSV file
    for row in table.find_all('tr'):
        csvwriter.writerow([cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])])

print(f"Table data saved to '{output_csv_path}'.")