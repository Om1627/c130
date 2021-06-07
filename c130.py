import csv
import pandas as pd
df=pd.read_csv("starsmerged.csv")
  

print(df.columns)
print(df.shape)
del df ["Luminosity"]

del df ["Unnamed: 0"]

print(df.columns)
df.to_csv("main.csv")