##Euler 47

##def npf(num):
##    # return a number prime factors of number
##    k = 2
##    a = set()
##    while k < num**0.5 or num == 1:
##        if num % k == 0:
##            num = num / k
##            a.add(k)
##            k -= 1
##        k += 1
##    return len(a)+1

def npf(num):
    ''' v2 return a number prime factors of number'''
    f = []
    while num % 2 == 0:
        if 2 not in f:
            f.append(2)
        num = num // 2
    for i in range(3, int(num**0.5)+1, 2):                
        while num % i == 0:
            if i not in f:
                f.append(i)
            num = num // i
    if num > 2:
        f.append(num)
    return len(f)

s = 2*3*5*7
while True:
    if all((npf(s)==4, npf(s+1)==4, npf(s+2)==4, npf(s+3)==4)):
        print(s-3) 
        break
    s += 1               
           





