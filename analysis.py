import datareader
from sklearn import linear_model
import matplotlib.pyplot as plt

#>>> Import the data as pandas dataframe
data = datareader.readCSV("avocado.csv")
data.set_index("ID", inplace=True)

#>>> Calculate mean avocado price for all countries:
avgPrice = data["AveragePrice"].mean()

#>>> Calculate avg price for each country
groupedData = data.groupby("region", as_index=False).mean()
groupedData = groupedData[["region", "AveragePrice"]]
#print(groupedData)

#>>> Get cheapest and most expensive region:
cheapReg = groupedData.min()
expReg = groupedData.max()
#print("Min: {} in {}, Max:: {} in {}".format(cheapReg["AveragePrice"], cheapReg["region"], expReg["AveragePrice"], expReg["region"]))

#>>> Regression for the prices over the years
X = data["year"]
Y = data["AveragePrice"]

linmod = linear_model.LinearRegression()
linmod = linmod.fit(X,Y)


# PANDAS functions
#Head: print(data.head())
#Tail: print(data.tail())
#Columns: print(data.region)
#List: print(data.region.tolist())
#Rows: for i, j in data.iterrows()
