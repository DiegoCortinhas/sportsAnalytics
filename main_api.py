from GithubConnector import GithubConnector
import json
import sys
import requests
import pandas as pd

github = GithubConnector()
years = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

dict_of_files = github.GetCsvRoundFilesUrlByYear(years)

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
