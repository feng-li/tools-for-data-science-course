Import pandas package import pandas as pd    
Define a dictionary containing employee data data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],         'Age':[27, 24, 22, 32],         'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}   
Convert the dictionary into DataFrame  df = pd.DataFrame(data)   
converting and overwriting values in column df["Name"]= df["Name"].str.lower()print(df)
replace().replace()
importing pandas module  import pandas as pd
Define a dictionary containing employee data data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],         'Age':[27, 24, 22, 32],         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'],         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
Convert the dictionary into DataFrame  df = pd.DataFrame(data)
dropping null value columns to avoid errors df.dropna(inplace = True)
new data frame with split value columns df["Address"]= df["Address"].str.split("a", n = 1, expand = True)
df display print(df)
importing pandas moduleimport pandas as pd
Define a dictionary containing employee datadata = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],        'Age':[27, 24, 22, 32],        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
Convert the dictionary into DataFramedf = pd.DataFrame(data)
making copy of address columnnew = df["Address"].copy()
concatenating address with name column
overwriting name columndf["Name"]= df["Name"].str.cat(new, sep =", ")
displayprint(df)
importing pandas module import pandas as pd
Define a dictionary containing employee data data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],         'Age':[27, 24, 22, 32],         'Address':['Nagpur junction', 'Kanpur junction',                    'Nagpur junction', 'Kannuaj junction'],         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
Convert the dictionary into DataFrame  df = pd.DataFrame(data)
replacing address name and adding spaces in start and end new = df["Address"].replace("Nagpur junction", "  Nagpur junction  ").copy()
checking with custom string print(new.str.strip()==" Nagpur junction")print(new.str.strip()=="Nagpur junction ")print(new.str.strip()==" Nagpur junction ")