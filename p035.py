##Euler 35
from numba import njit

@njit
def is_prime6(n):
    #return True, if number is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def is_circular_prime(n):
    #return number, if all rotations of digits are primes, 123-312-231 
    if is_prime6(n):
        if len(str(n)) == 1:
            return n
        else:
            for i in range(1, len(str(n))):
                rotation = int(f'{n%(10**i)}{n//(10**i)}')
                if not is_prime6(rotation):
                    return None
            return n

def comp():
    #mainloop
    count = 0
    for i in range(1, 1_000_000):
        if is_circular_prime(i):
            count += 1
    return count
    
if __name__ == '__main__':    

    print(comp())
             
