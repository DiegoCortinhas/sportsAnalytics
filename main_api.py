from GithubConnector import GithubConnector
from CsvReader import CsvReader
import json, sys, requests
import pandas as pd

github = GithubConnector()
csv_reader = CsvReader()

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020]

dict_of_files = github.GetCsvRoundFilesUrlByYear(years)

# Ler os dataframes dos arquivos
list_of_dataframes = []

for key, item in dict_of_files.items():
    csv_data = github.CsvDownload(item)
    csv_reader.ReadCsvFile(csv_data)

    #df = pd.read_csv(item)
    #df['rodada'] = key
    #list_of_dataframes.append(df)


# cursor.execute('INSERT INTO testcsv(names, \
#         classes, mark )' \
#         'VALUES("%s", "%s", "%s")', 
#         row)
# #close the connection to the database.
# mydb.commit()
# cursor.close()
# print "Done"

# Combinar lista de DataFrames criados
cartola = pd.concat(list_of_dataframes)
print(cartola.shape)
cartola.shape

# Ver informações do dataframe
cartola.info()
