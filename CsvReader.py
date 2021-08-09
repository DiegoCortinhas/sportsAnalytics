import csv, sys
from DbConnector import DbConnector

class CsvReader:
    
    def ReadCsvFile(self, csv_data):
        connector = DbConnector()

        cr = csv.reader(csv_data, delimiter=',')
        my_list = list(cr)
        count = 1

        for row in my_list:
            #ignora a primeira linha de cabeçalho de cada arquivo do csv
            if count != 1:
                connector.InsertBanco(tuple(row))
                print(row)
                print("Inserindo linha " + str(count))
                #sys.exit()
            count += 1

