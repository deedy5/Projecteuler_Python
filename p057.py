##Euler 57
##Square root convergents
from fractions import Fraction

p = 1
q = 1
count = 0
for i in range(1000):    
    n = p + 2*q
    d = p + q
    if len(str(n)) > len(str(d)):
        count += 1
    p = n
    q = d
print(count)

