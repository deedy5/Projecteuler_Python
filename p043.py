##Euler 43
from itertools import permutations

d_list = [1, 2, 3, 5, 7, 11, 13, 17]
summ = 0

for x in permutations('0123456789'):
   for k in range(1, 8):
      if int(''.join(x)[k:k+3]) % d_list[k] != 0:
         break
   else:     
      summ += int(''.join(x))
      
print(f'{summ = }')
