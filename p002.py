# fibonacci list [a] ( < 4_000_000)
a = [1,2]
[a.append(a[-1]+a[-2]) for x in range(2000) if (a[-1]+a[-2])<=4_000_000]

# fibonacci list [b] ( % 2 == 0)
b = [x for x in a if x%2==0]

print(sum(b))
    
