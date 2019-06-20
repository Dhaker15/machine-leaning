import numpy as np
import random

x=int(input('enter no, of rows='))
y=int(input('enter mo. of colom='))
z=np.random.random((x,y))
z
np.savetxt('array.txt',z)

