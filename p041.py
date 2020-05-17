##Euler 41
from itertools import permutations
import math

def is_prime6(n):
   #Primarility test   
   if n <= 1:
      return False
   if n <= 3:
      return True
   if n % 2 == 0 or n % 3 == 0:
      return False    
   for i in range(5, math.isqrt(n)+1, 6):
      if n % i == 0 or n % (i + 2) == 0:
         return False
   return True
         
for i in range(9):
   for x in permutations('987654321'[i:]):      
      test = int(''.join(x))
      if is_prime6(test):
         print(f'{test}')  
         break
   else:
      continue
   break
   
   

  



















              
     




            
