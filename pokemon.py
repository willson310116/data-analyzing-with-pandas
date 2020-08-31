import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
##
# Read data from csv save as DataFrame
df = pd.read_csv('pokemon.csv')
# Show every columns in the DataFrame
pd.set_option('display.max_columns', None)

# def head(DataFrame):
# 	print(DataFrame.head())
# head(df)
#print(df.head())
#df.head()
# df.info()
# print("-------------------------------")
# print(df.info())

print(df.corr())

#correlation map
f,ax = plt.subplots(figsize=(15, 8))
#df.corr()
sns.heatmap(df.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax,cmap='YlGnBu')
#plt.show()

#df.columns
print(df['Legendary'].value_counts(dropna =False))

# 把 Type 2 是 NaN 用他自己的 Type 1 代替
df["Type 2"] = df["Type 2"].replace(np.nan, df["Type 1"])

df = df[~df["Name"].isnull()].reset_index(drop=True) 
#把遺漏的一筆刪掉，原本800筆資料->799筆
#df.info()

df = df.drop(["#"],axis=1)
#df = df.drop(["#"],axis=1)
df.info()



