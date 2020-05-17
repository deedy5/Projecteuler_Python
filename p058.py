##Euler 58
##Spiral primes
import time
from prime6 import is_prime6

def main():
    count_all = 1
    count = 0
    for n in range(2, 1000000):
        x = 4*n**2 - 6*n +3
        y = 4*(n-1)**2 + 1
        z = 4*n**2 - 10*n + 7
        s = 2*(n-1) + 1        
        count_all += 4
        if is_prime6(x):
            count += 1
        if is_prime6(y):
            count += 1
        if is_prime6(z):
            count += 1
        r = count/count_all * 100
        if r < 8:
            return s
        
start = time.time()
result = main()
print(f'{result} in {time.time()-start}')



