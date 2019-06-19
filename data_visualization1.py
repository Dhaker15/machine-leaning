#!/bin/python3

import matplotlib.pyplot as plt
import pandas as ps

df=ps.read_csv('student.csv')
df

plt.pie(df.iloc[:,1],labels=df.iloc[:,0],explode=(0.3,0,0,0.9,0))

plt.show()

