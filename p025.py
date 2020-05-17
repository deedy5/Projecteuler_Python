##Euler 25

f_s = [0, 1, 1,]
for i in range(3, 1000000000):
    f_s.append(f_s[i-1] + f_s[i-2])    
    if len(str(f_s[i])) == 1000:
        print(i)        
        break

    





