import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

#Now predictig the values data from the scaled data
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()#Creating a scaling object

df = pandas.read_csv("data.csv")#reading data.csv

X = df[['Weight', 'Volume']]#extracting the column weight and volume
y = df['CO2']#Extracting the co2 column

scaledX = scale.fit_transform(X)#calculating the mean and std and scaling to store in scaledx object

regr = linear_model.LinearRegression()#creating a empty learning model
regr.fit(scaledX, y)#giving two data inputs so it can find or learn relationship


scaled = scale.transform([[2300, 1.3]])#providing the new data for calculation of co2

predictedCO2 = regr.predict([scaled[0]])#2D array input requires and selects the first value
print(predictedCO2)#Gives output