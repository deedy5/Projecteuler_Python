##Euler 36

def is_palindrome_n_b(num):
    return num == int(f'{num}'[::-1]) and f'{num:b}' == f'{num:b}'[::-1]

result = sum([x for x in range(1, 1000000) if is_palindrome_n_b(x)])
print(result)



            
