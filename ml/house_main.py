import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
house=pd.read_csv('house.csv')
X=house[['bedrooms','bathrooms','sqft_living', 'sqft_lot','floors','sqft_above',
         'sqft_lot15','yr_built','condition','zipcode']]
y=house['price']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)     #it will train the model using training data set
predict=model.predict(X_test)
#house1=house[house['id']==6414100192 ]
#print(house1['price'])
model.coef_  #coeff for our features that is X
df=pd.DataFrame(model.coef_,X.columns,columns=['coff. values'])
model.intercept_ #y intercept
from sklearn import metrics
mse=metrics.mean_squared_error(y_test,predict)
rsme=np.sqrt(mse)
#print(rsme)

#------------------------------------------------------------------Training new model-------------------------------------------

X=house[['bedrooms','bathrooms','sqft_living', 'sqft_lot',
         'yr_built','zipcode']]
y=house['price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)
model2=LinearRegression()
model2.fit(X_train,y_train)
predict2=model2.predict(X_test)
mse2=metrics.mean_squared_error(y_test,predict2)
smse2=np.sqrt(mse2)
#print(smse2)

#-----------------------------------------------------------------Training new model--------------------------------------------

X=house[['bedrooms','bathrooms','view','bedrooms','bathrooms','sqft_living', 'sqft_lot','floors','sqft_above',
         'sqft_lot15','yr_built','condition','zipcode','condition']]
y=house['price']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)
model3=LinearRegression()
model3.fit(X_train,y_train)
predict3=model3.predict(X_test)
mse3=metrics.mean_squared_error(y_test,predict3)
smse3=np.sqrt(mse3)
#plt.plot(y_test,predict)
print("Minimum root mean squared error : " , min(smse3,smse2,rsme))
#plt.plot(y_test,predict2)
plt.plot(y_test,predict3)
plt.savefig('pred3.pdf')
