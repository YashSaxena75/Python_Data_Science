import quandl
import pandas as pd

df=quandl.get("ZILLOW/C26168_ZHVISF", authtoken="s4szyQkyTGQP9pmDuTEu")

#print(df.head())

states=pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print(states[0][0])
