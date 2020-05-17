##Euler 27
def is_prime6(n):
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

max_n = 0
max_a = 0
max_b = 0
for a in range (-999, 1000):
    for b in range (-1000, 1001):
        n = 0   
        while is_prime6(n*n + a*n + b):
            n += 1            
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b

print(f'Max n = {max_n}. a = {max_a}, b = {max_b}, a*b = {max_a*max_b}')


