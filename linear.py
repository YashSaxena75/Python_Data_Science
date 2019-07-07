import pandas as pd
import numpy as np
from sklearn import preprocessing,svm,model_selection
from sklearn.linear_model import LinearRegression
import quandl,math

df=quandl.get('WIKI/GOOGL')

df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forec='Adj. Close'
df.fillna(-99999,inplace=True) #remove Nan by -99999 bcz we can't proceed without a number i.e. with a Nan

forc=math.ceil(0.01*len(df))
forc=int(forc)
print(forc)

df['label']=df[forec].shift(-forc)
df.dropna(inplace=True)
#print(df.head())
#print("----------------------------------------------------------------------------------------------")
#print(df.tail())
x=np.array(df.drop(['label'],1))
y=np.array(df['label'])

y=preprocessing.scale(y)
#x=x[:-forc]
#df.dropna(inplace=True)
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2)
clf=LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)
acc=clf.score(x_test,y_test)

print(acc)
