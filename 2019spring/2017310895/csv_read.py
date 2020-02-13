import pandas
data = pandas.read_csv("93#乙醇.csv",delimiter="\t",header = None)
print(len(data))
print(type(data))
