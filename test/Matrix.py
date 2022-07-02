from email.utils import collapse_rfc2231_value
import numpy as np
import time
import ray

ray.init(address="192.168.43.247:6379")

def f1():
    n = 1200
    a = np.random.randint(0, 10, (n, n))
    b = np.random.randint(0, 10, (n, n))
    c = a @ b

@ray.remote
def f2():
    n = 1200
    a = np.random.randint(0, 10, (n, n))
    b = np.random.randint(0, 10, (n, n))
    c = a @ b

time1=time.time()
[ f1() for _ in range(8)]
print(time.time()-time1)

time2=time.time()
ray.get([ f2.remote() for _ in range(8)])
print(time.time()-time2)