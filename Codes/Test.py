#Checking NUll Values
import pandas as pd
data=pd.read_csv("/Users/jayadeep/Desktop/Prep/Facebook_EDA/FB_Data.csv")
print(data.isnull().sum())
print((data == "").sum())
print((data == "Unknown").sum())



