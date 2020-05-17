##Euler 14
    
dic = {n: 0 for n in range(1, 1_000_000)}
dic[1] = 1
dic[2] = 2

for n in range(3, 1_000_000):
    counter = 0
    original_number = n

    while n > 1:
        if n < original_number:
            dic[original_number] = dic[n] + counter
            break
        if n%2 == 0:
            n = n/2
            counter += 1
        else:
            n = 3*n+1
            counter+=1           

print(list(dic.values()).index(max(dic.values()))+1)

