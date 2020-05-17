##Euler 46
def primes_generator(limit):
    #sieve of Eratosthenes    
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def twices_squares_generator(lim):
    return (2*(i*i) for i in range(1, lim))

primes = [x for x in primes_generator(100_00)]
twices_squares = [x for x in twices_squares_generator(100_00)]
set_odd_comps = set(x for x in range(9, 100_00, 2)) - set(primes)
odd_comps = sorted(list(set_odd_comps))
set_sum = set(x+y for x in primes for y in twices_squares)
result_set = set_odd_comps - set_sum
result = sorted(list(result_set))[0]
      
print(f'{result = }')

