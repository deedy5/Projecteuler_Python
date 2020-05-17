##Euler 52
import time

def func():
    for x in range(1, 1_000_000):
        if set(str(x)) == set(str(x*2)) == set(str(x*3)) ==\
           set(str(x*4)) == set(str(x*5)) == set(str(x*6)):
            return x
        
start = time.time()
print(f'{func()} in {time.time()-start}')      











