import numpy as np
import time
import ray



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

def main():
    ray.init()
    time1=time.time()
    [ f1() for _ in range(8)]
    print(time.time()-time1)
    time2=time.time()
    ray.get([ f2.remote() for _ in range(8)])
    print(time.time()-time2)


if __name__ == '__main__':
    main()
