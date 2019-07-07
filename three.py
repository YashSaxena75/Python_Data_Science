import pandas as pd
df=pd.read_csv('/root/Desktop/ML/data.csv')
#df.set_index('Date',inplace=True)
#df.to_csv('/root/Desktop/ML/data2.csv')
#print(df.head())

fd=pd.read_csv('/root/Desktop/ML/data2.csv',index_col=0)

#print(fd.head())
fd.columns=['Austin']

df.to_csv('/root/Desktop/ML/data3.csv')

data=pd.read_csv('/root/Desktop/ML/data3.csv')
df.to_html('/root/Desktop/ML/data4.html')

da=pd.read_html('/root/Desktop/ML/data4.html',index_col=0)
print(da)

