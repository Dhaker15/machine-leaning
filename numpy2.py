import numpy as np

a=np.arange(100,125,1)
for i in a :
  j=i+80
  b=np.arange(i,j,5).reshape(8,2)
  print(b)

