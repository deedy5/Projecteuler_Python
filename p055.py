##Euler 55
##Lychrel numbers

import time

def is_lichrel(number):
    for _ in range(50):
        number += int(f'{number}'[::-1])
        if number == int(f'{number}'[::-1]):
            return False
    return True

start = time.time()
r = sum(is_lichrel(x) for x in range(10000))
print(f'{r} in {time.time()-start}')




