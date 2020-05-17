##Euler 5
from numba import njit

@njit
def comp():
    count = 0
    n = 1
    while count < 19:
        count = 0
        for j in range (2, 21):
            if n % j ==0:
                count += 1
            else:
                n+=1
    return n

print(comp())


        
    
        

