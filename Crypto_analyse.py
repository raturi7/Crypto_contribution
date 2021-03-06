import numpy as np
import pandas as pd

ada=pd.read_csv("../input/crypto-data/ada_data.csv",index_col=0)
ada.rename(columns={"0" : "Date",
           "1":"Price"},inplace = True)
ada['Date'] = pd.to_datetime(ada['Date'])
ada.head()

btc=pd.read_csv("../input/crypto-data/btc_data.csv",index_col=0)
btc.rename(columns={"0" : "Date",
           "1":"Price"},inplace = True)
btc['Date'] = pd.to_datetime(btc['Date'])
btc.head()

eth=pd.read_csv("../input/crypto-data/btc_data.csv",index_col=0)
eth.rename(columns={"0" : "Date",
           "1":"Price"},inplace = True)
eth['Date'] = pd.to_datetime(eth['Date'])
eth.head()

print(ada.describe(),"\n\n")
print("----------------------------------------------------------------------\n")
print("Mean = ",ada.Price.mean(),"\n")
print("----------------------------------------------------------------------\n")
print("Size = ",ada.size,"\n")
print("----------------------------------------------------------------------\n")
print("Shape = ",ada.shape,"\n\n")
print("----------------------------------------------------------------------\n")
print("Price = \n", ada.Price.unique(),"\n")
print("----------------------------------------------------------------------\n")
print(ada.Date.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(ada.Price.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(ada.info(),"\n")
print("----------------------------------------------------------------------\n")
ada.Price.map(lambda p: p - ada.Price.mean())

print(btc.describe(),"\n\n")
print("----------------------------------------------------------------------\n")
print("Mean = ",btc.Price.mean(),"\n")
print("----------------------------------------------------------------------\n")
print("Size = ",btc.size,"\n")
print("----------------------------------------------------------------------\n")
print("Shape = ",btc.shape,"\n\n")
print("----------------------------------------------------------------------\n")
print("Price = \n", btc.Price.unique(),"\n")
print("----------------------------------------------------------------------\n")
print(btc.Date.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(btc.Price.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(btc.info(),"\n")
print("----------------------------------------------------------------------\n")
btc.Price.map(lambda p: p - btc.Price.mean())

print(eth.describe(),"\n\n")
print("----------------------------------------------------------------------\n")
print("Mean = ",eth.Price.mean(),"\n")
print("----------------------------------------------------------------------\n")
print("Size = ",eth.size,"\n")
print("----------------------------------------------------------------------\n")
print("Shape = ",eth.shape,"\n\n")
print("----------------------------------------------------------------------\n")
print("Price = \n", eth.Price.unique(),"\n")
print("----------------------------------------------------------------------\n")
print(eth.Date.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(eth.Price.value_counts(),"\n")
print("----------------------------------------------------------------------\n")
print(eth.info(),"\n")
print("----------------------------------------------------------------------\n")
eth.Price.map(lambda p: p - eth.Price.mean())
