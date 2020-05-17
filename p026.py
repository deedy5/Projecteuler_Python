##Euler 26

def recurring_cycle(d):    
    for length in range(1, d):        
        if pow(10, length, d) == 1:            
            return length
    return 0

longest, i = max((recurring_cycle(i),i) for i in range(2,1001))
print(i)



    



