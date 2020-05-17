##Euler 40
import math

r = ''.join([str(x) for x in range(200_000)])
result = math.prod([int(r[10**i]) for i in range(7)])

print(f'result = {result}')
      




            
