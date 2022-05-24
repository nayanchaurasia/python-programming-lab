import numpy
import numpy as np
m=[[5,6],[4,7]]
r=len(m)
c=len(m[0])
if r==c:
    print(np.trace(m))
else:
    print('the matrix is not a square matrix therefore no sum of diagonal elements')