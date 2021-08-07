from data import *
import csv
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://github.com/henriquepgomide/caRtola/tree/master/data/2019'
html = requests.get(URL)
soup = BeautifulSoup(html.text, 'lxml')
result = []
for tag in soup.find_all('a', href=True):
    result.append(tag)
result[70:90:2]

regex = 'rodada-([0-9]|[0-9][0-9])\.csv'

dict_of_files = {}

for tag in soup.find_all('a', attrs={'href': re.compile(regex)}):
    href_str = tag.get('href')
    file_name = re.sub('/henriquepgomide/caRtola/blob/master/data/2019/', '', href_str)
    file_url = re.sub('/henriquepgomide/caRtola/blob/master/data/2019/',
                      'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/2019/', href_str)
    dict_of_files[file_name] = file_url

# Ler os dataframes dos arquivos
list_of_dataframes = []
for key, item in dict_of_files.items():
    df = pd.read_csv(item)
    df['rodada'] = key
    list_of_dataframes.append(df)

# Combinar lista de DataFrames criados
cartola = pd.concat(list_of_dataframes)
cartola.shape()

# Ver informações do dataframe
cartola.info()
