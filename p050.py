##Euler 50
##Consecutive prime sum

##v1
##import prime6
##def main():
##    plist = prime6.sieve6(4000)
##    mc = 0      # max count
##    ms = 0      # max summ
##    for i in range(len(plist)):
##        for j in range(i, len(plist)):
##            
##            ts = sum(plist[i:j])
##            if ts < 1_000_000:
##                count = len(plist[i:j])        
##                if prime6.is_prime6(ts) and count > mc:
##                    ms = ts
##                    mc = count
##    return ms      
##print(main())

##################################################
##v2
from prime6 import is_prime6
import time

def sieve6g(limit):
    #sieve of Eratosthenes generator    
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def comp():
    plist = [(0, 0)]
    sumn = 0
    for x in sieve6g(4000):
        sumn += x
        plist.append((x, sumn))
    mc = 0      # max count
    ms = 0      # max summ
    for i in range(1, len(plist)):
        for j in range(i, len(plist)):            
            ts = plist[j][1] - plist[i-1][1]
            if ts < 1_000_000:
                count = j - i
                if is_prime6(ts) and count > mc:
                    ms = ts
                    mc = count
    return ms


print(comp())









