import numpy
import numpy as np
m=[[1,2],[3,4]]
m1=np.array(m)
print(m1)
print(m1.reshape(1,4))
out=np.transpose(m1)
print(out)