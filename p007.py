##Euler 7
n = 1000000
c = int(n ** 0.5)

a = [True] * n

for i in range(2, c):   
    for j in range(i*i, n, i):
        a[j] = False

b = [i for i in range(2, n) if a[i]]

print(b[10000])
