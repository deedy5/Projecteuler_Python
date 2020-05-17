##Euler 30

cache = {0:0}
result = []
    
def sum_pows(number):
    summ = 0
    for i in list(str(number)):
        if i not in cache:
            cache[i] = int(i)**5
        summ += cache[i]
    if summ == number:
        return summ


result = sum([x for x in range(11, 999999) if sum_pows(x)])

print(result)



