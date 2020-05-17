##Euler 62
##Cubic permutations
import time

def compute():
    cache = {}
    for i in range(405, 10000):
        n = i*i*i
        sn = ''.join(sorted(f'{n}'))
        if sn not in cache:
            cache[sn] = [n]
        else:
            cache[sn].append(n)
        if len(cache[sn]) == 5:
            return min(cache[sn])
        
        
start = time.time()
result = compute()
print(f'{result} in {time.time()-start}')




