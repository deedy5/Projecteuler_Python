##Euler 39
import math

dic = {x:[] for x in range(1000)}

for a in range(1, 1000):
    for b in range(a, 1000):
        count = 0
        c = math.hypot(a, b)
        if c % 1 == 0:
            c = math.ceil(c)
            p = a + b + c            
            if p < 1000:
                dic[p].append((a, b, c))               

result = max([(len(v), k) for k,v in dic.items()])
print(f'p = {result[1]}. solutions = {result[0]}')        



                


    




















              
##print(f'S{result} in {time.time() - start} sec.')       




            
