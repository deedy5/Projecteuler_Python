##Euler 60
from prime6 import is_prime6, sieve6
import time

def is_pp(x, y):
    '''
    aka is_prime_pair - return True if concatenations
    of x and y all are prime numbers
    '''
    return is_prime6(int(f'{x}{y}')) and is_prime6(int(f'{y}{x}'))        

def main():
    p = sieve6(10_000)
    rlist = []
    for i1 in range(len(p)):
        for i2 in range(i1, len(p)):            
            if is_pp(p[i1], p[i2]):
                
                for i3 in range(i2, len(p)):                    
                    if is_pp(p[i1], p[i3]) and \
                       is_pp(p[i2], p[i3]):
                        
                        for i4 in range(i3, len(p)):                            
                            if is_pp(p[i1], p[i4]) and \
                               is_pp(p[i2], p[i4]) and \
                               is_pp(p[i3], p[i4]):
                                
                                for i5 in range(i4, len(p)):                                    
                                    if is_pp(p[i1], p[i5]) and \
                                       is_pp(p[i2], p[i5]) and \
                                       is_pp(p[i3], p[i5]) and \
                                       is_pp(p[i4], p[i5]):
                                        
                                        rlist.append([p[i1], p[i2], p[i3], p[i4], p[i5]])
                                        return sum(rlist[0])
    
start = time.time()
print(f'{main()} in {time.time()-start}')

