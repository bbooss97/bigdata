import numpy as np
coefficients=np.array([float(x) for x in input().split()])
print(np.polyval(coefficients,int(input())))