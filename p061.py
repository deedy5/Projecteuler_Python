##Euler 61
##Cyclical figurate numbers

from itertools import permutations
import time

def calc():
    for p in permutations(list_all):
        for n0 in p[0]:
            for n1 in p[1]:
                if n0 // 100 == n1 % 100:
                    
                    for n2 in p[2]:
                        if n1 // 100 == n2 % 100:

                            for n3 in p[3]:
                                if n2 // 100 == n3 % 100:

                                    for n4 in p[4]:
                                        if n3 // 100 == n4 % 100:

                                            for n5 in p[5]:
                                                if n4 // 100 == n5 % 100 and \
                                                   n5 // 100 == n0 % 100:
                                                    return sum([n0, n1, n2,
                                                                n3, n4, n5])
                                                    
start = time.time()

list3 = [x for n in range(1, 150) if 999 < (x := n*(n+1)//2) < 10000]
list4 = [x for n in range(1, 150) if 999 < (x := n*n) < 10000]
list5 = [x for n in range(1, 150) if 999 < (x := n*(3*n-1)//2) < 10000]
list6 = [x for n in range(1, 150) if 999 < (x := n*(2*n-1)) < 10000]
list7 = [x for n in range(1, 150) if 999 < (x := n*(5*n-3)//2) < 10000]
list8 = [x for n in range(1, 150) if 999 < (x := n*(3*n-2)) < 10000]
list_all = [list3, list4, list5, list6, list7, list8]

result = calc()
print(f'{result} in {time.time()-start}')          





