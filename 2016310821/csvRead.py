# practice:
# pandas.read_csv
# zipfile, myzip.open()

import pandas
import zipfile

data1 = pandas.read_csv('stocks.csv')

myzip = zipfile.ZipFile('stocks.zip')
data2 = pandas.read_csv(myzip.open('stocks.csv'))
myzip.close()
