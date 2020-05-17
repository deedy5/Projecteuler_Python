##Euler 49
from itertools import permutations

def is_prime6(n):
   #Primarility test   
   if n <= 1:
      return False
   if n <= 3:
      return True
   if n % 2 == 0 or n % 3 == 0:
      return False    
   for i in range(5, int(n**0.5) + 1, 6):
      if n % i == 0 or n % (i + 2) == 0:
         return False
   return True


for i in range(1489, 10000, 2):        
    if is_prime6(i) and is_prime6(i+3330) and is_prime6(i+6660):
        if set(''.join(x) for x in permutations(str(i))) ==\
           set(''.join(y) for y in permutations(str(i+3330))) ==\
           set(''.join(z) for z in permutations(str(i+6660))):
            print(f'result: {i}{i+3330}{i+6660}')
            break   





