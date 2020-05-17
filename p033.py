##Euler 33

from fractions import Fraction

result = 1
for x in range(10, 100):
    for y in range(x+1, 100):
        if str(x)[1] == str(y)[0]:
            if str(y)[1] == '0':
                continue
            else:
                if Fraction(x, y) == Fraction(int(str(x)[0]), int(str(y)[1])):
                    result *= Fraction(x, y)
                    
print(result.denominator)

        
##d = 1
##for i in range(1, 10):
##    for j in range(1, i):
##        q, r = divmod(9*j*i, 10*j-i)
##        if not r and q <= 9:
##            d *= i/float(j)
##
##print("Project Euler 33 Solution =", d)




