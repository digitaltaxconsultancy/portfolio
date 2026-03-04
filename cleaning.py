import pandas as pd

df = pd.read_csv("IBM_HR_Employee_Attrition_Data.csv")
df.isnull().sum()
df.duplicated().sum()