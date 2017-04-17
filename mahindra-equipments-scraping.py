import requests
import csv
from bs4 import BeautifulSoup
# url = 'https://www.mahindratractor.com/tractor-mechanisation-solutions/yuvo/mahindra-yuvo-275-di'
url = input("Enter ul to extract: ")
File_name = input("Enter the file name: ")
File_name = File_name +".csv"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('tbody')
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
import pandas as pd
my_df = pd.DataFrame(list_of_rows)
my_df.to_csv(File_name, index=False, header=False)
print("File saved as " + File_name)
