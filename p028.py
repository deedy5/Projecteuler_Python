##Euler 28

number = 1
summ = 1
step = 2
for i in range(1, 5, 2):
    for j in range(4):
        number += step
        summ += number       
    step += 2   

print(summ)
