##Euler 34
from functools import lru_cache
from concurrent.futures import ProcessPoolExecutor


@lru_cache
def factorial(x):
    if x < 2:
        return 1
    return x * factorial(x-1)

def is_curious(n):
    summ = 0
    for i in list(str(n)):
        summ += factorial(int(i))
    if summ == n:
        return n
    
def comp():
    summ = 0
    with ProcessPoolExecutor() as executor:
        worklist = (i for i in range(3, 362880 * 9))
        for result in executor.map(is_curious, worklist, chunksize=3000):
            if result:
                summ += result
    return summ
                
if __name__ == '__main__':   
    print(comp())



####v2
##from math import factorial
##print(sum(n for n in range(10,100000) if n==sum(factorial(int(a)) for a in str(n))))


####v3
##summ = 0
##for n in range(10, 100000):
##    summ_f = 0
##    for a in str(n):
##        f = factorial(int(a))
##        summ_f += f
##        if n == summ_f:
##            summ += n
##print(summ)
    
            
