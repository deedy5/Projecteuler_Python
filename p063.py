##Euler 63
##Powerful digit counts
import time

def compute():
    cache = set()
    for i in range(1, 22):
        for j in range(1, 10):
            n = j**i
            if len(f'{n}') == i:
                cache.add(n)
    return len(cache)
   

       
start = time.time()
result = compute()
print(f'{result} in {time.time()-start}')





