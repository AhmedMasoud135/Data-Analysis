import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max.columns',20)



# Read the data
data = pd.read_csv(r"salesforcourse-4fe2kehu.csv")
data.info()


# Clean the data
data.columns[data.isnull().any()]
data.drop(columns="Column1",inplace=True)
data.dropna(inplace=True)



# Add Profit column
data["Check"] = data["Revenue"] >= data["Cost"]
data["Check"].value_counts()                    # 4854 False value these values are incorrect values as no negative profit
x = data.loc[data["Check"] == False]            # drop these values
data.drop(x.index , inplace = True)
data["Profit"] = data["Revenue"] - data["Cost"]
data.head()



# Drop 
data.drop(columns=["Cost","Revenue","Unit Price","Check"],inplace=True)


# Rename 
data.rename(columns={"index":"ID"},inplace=True)



# Save the new data
data.to_csv("NEWData.csv",index=False)