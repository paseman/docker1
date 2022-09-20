from time import time
import numpy as np

def timeTest(n):
  start_time=time()
  np.array(range(n)).cumprod()
  print("cumprod of %d is %f "%(n,time() - start_time))

timeTest(1000)
timeTest(1000000)
timeTest(1000000000)
