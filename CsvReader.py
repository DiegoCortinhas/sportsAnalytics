import csv, sys

class CsvReader:
    
    def ReadCsvFile(self, csv_data):
        cr = csv.reader(csv_data, delimiter=',')
        my_list = list(cr)
        i = 1
        for row in my_list:
            print(row)
            if i == 2:
                sys.exit()
            i += 1