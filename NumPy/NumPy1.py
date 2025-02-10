#! C:\Users\hardi\OneDrive\Documents\GitHub\Hardik\MyVirtualEnvironment\Scripts\python.exe

import numpy as np
import time

start_time = time.time()

a = [i for i in range(100000000)]
b = [i for i in range(100000000, 200000000)]
c = []

for i in range (len(a)):
    c.append(a[i]+b[i])

print (time.time() - start_time)

start_time = time.time()

a=np.arange(100000000)
b=np.arange(100000000, 200000000)

c=a+b

print (time.time() - start_time)