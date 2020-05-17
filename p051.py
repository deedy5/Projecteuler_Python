##Euler 51
from prime6 import *
import time

def epf(num, rd):
    count = 0
    for dig in '0123456789':
        n = int(num.replace(rd, dig))
        if n > 100_000 and is_prime6(n):
            count += 1
    return count == 8

def main():
    plist = sieve6(1_000_000)
    for prime in plist:
        if prime >100_000:
            s = str(prime)
            if s.count('0') == 3 and epf(s, '0') or\
               s.count('1') == 3 and epf(s, '1') or\
               s.count('2') == 3 and epf(s, '2'):
                return s
            
start = time.time()
r = main()
print(f'{r} in {time.time()-start}')






