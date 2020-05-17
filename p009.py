##Euler 9

def pithagor_triplet(n):
    for a in range(n):
        for b in range(a+1, n):
            c = n - a - b
            if c > 0 and c > b:
                if a*a + b*b == c*c:
                    return(a*b*c)
                 
print(pithagor_triplet(1000))


        



    
    







