##Euler 56
##Powerful digit sum

import time

def sum_d(n):
    return sum([int(x) for x in str(n)])

start = time.time()
r = max([sum_d(a**b) for a in range(100) for b in range(100)])
print(f'{r} in {time.time()-start}')



