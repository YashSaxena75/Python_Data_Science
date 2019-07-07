import pandas as pd
import datetime,numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

webs={'day':[1,2,3,4,5,6],
      'Visitors':[43,53,34,45,64,34],
      'BRate':[65,72,62,64,54,66]}

df=pd.DataFrame(webs)
#print(df.BRate)
print(np.array(df[['day','BRate']]))
