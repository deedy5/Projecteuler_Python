a =600851475143
div = 0
s = []

for i in range(1, a+1):
    if a % i == 0:
        div = a / i        
        a = div
        s.append(a)
        if a == 1:
            break
        
print(s[-2])


        
        
   
        


