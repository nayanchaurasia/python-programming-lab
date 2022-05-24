import numpy as np
l=np.arange(0,10)
print(l)
m=np.array(l,ndmin=3)
print(m)
#2-D array to 1-D array
m1=m.reshape(1,10)
print(m1)
# 1-D array to 2*5 D array
m2=m.reshape(2,5)
print(m2)