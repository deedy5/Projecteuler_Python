##Euler 37
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

def is_truncatable_prime(n):
    #return number, if all of truncs of number are primes, 3797-797-97-7-379-37-3 
    if is_prime6(n):
        if len(str(n)) >= 2:
            for i in range(1, len(str(n))):
                trunc1 = n % (10**i)
                trunc2 = n // (10**i)
                if not is_prime6(trunc1) or not is_prime6(trunc2):
                    return None
            return n

    
if __name__ == '__main__':
    

    result = sum(i for i in range(1, 1_000_000) if is_truncatable_prime(i))            
    print(f'Sum = {result}')       




            
