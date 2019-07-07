import pandas as pd,datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing,svm,model_selection
from sklearn.linear_model import LinearRegression
import quandl,math
from matplotlib import style

df=quandl.get('WIKI/GOOGL')
style.use('ggplot')
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100
df['PCT_change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100

df=df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col='Adj. Close'
df.fillna(-99999,inplace=True) #remove Nan by -99999 bcz we can't proceed without a number i.e. with a Nan

forcast_out=math.ceil(0.01*len(df))
forcast_out=int(forcast_out)
print(forcast_out)

df['label']=df[forecast_col].shift(-forcast_out)
#df.dropna(inplace=True)
x=np.array(df.drop(['label'],1))
x=x[:-forcast_out]
x_lately=x[-forcast_out:]
x=preprocessing.scale(x)
df.dropna(inplace=True)
y=np.array(df['label'])
y=np.array(df['label'])
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2)
clf=LinearRegression(n_jobs=-1)
clf.fit(x_train,y_train)
acc=clf.score(x_test,y_test)

forecast_set=clf.predict(x_lately)
print(forecast_set,acc)

df['forecast']=np.nan

ldate=df.iloc[-1].name

last_unix=ldate.timestamp()

oday=86365

nunix=last_unix+oday

for i in forecast_set:
	ndate=datetime.datetime.fromtimestamp(nunix)
	df.loc[ndate]=[np.nan for _ in range (len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
