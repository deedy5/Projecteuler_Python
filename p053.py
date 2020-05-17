##Euler 53
import math
import time

start = time.time()
count = 0
for n in range(23, 101):
    for r in range(n):
        if math.comb(n, r) > 1_000_000:
            count += 1

print(f'{count} in {time.time()-start}')








