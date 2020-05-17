##Euler 31
s = [1] + [0]*200

for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for i in range(len(s) - coin):
        s[i+coin] += s[i]
        
print(f'{s[-1]}')


