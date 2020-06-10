import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set(color_codes=True)
ethprice = [208.16, 205.96, 203.65, 208.22, 206.06, 211.38, 213.32]
prices1 = pd.DataFrame ([[8812.95,208.16],[8845.67,205.96], [8843.9,203.65], [9272.37,208.22], [9517.01,206.06], [9939.29,211.38], [9817.29,213.32]])
sns.regplot(x=bitprice, y=ethprice, data=prices1);
