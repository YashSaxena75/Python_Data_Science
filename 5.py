import pandas as pd

df1=pd.DataFrame({'HPI':[80,85,88,85],
		  'Rate':[2,3,2,2],
		  'GDP':[50,55,65,55]},
		 index=[2001,2002,2003,2004])

df2=pd.DataFrame({'HPI':[80,85,88,85],
                  'Rate':[2,3,2,2],
                  'GDP':[50,55,65,55]},
		 index=[2005,2006,2007,2008])

df3=pd.DataFrame({'HPI':[80,85,88,85],
                  'Rate':[2,3,2,2],
                  'GDP':[50,52,50,53]},
		 index=[2001,2002,2003,2004])

#concat=pd.concat([df1,df2,df3])
#print(concat)

df4=df1.append(df3)

print(df4)
