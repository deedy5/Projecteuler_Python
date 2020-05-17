##Euler 20

def factorial(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial

x = factorial(100)
print(sum(map(int, str(x))))
        
