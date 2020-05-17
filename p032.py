##Euler 32

cache = set()

def is_pan_mult(x, y):
    if ''.join(sorted(f'{x}{y}{x*y}')) == '123456789':
        return x * y        

for x in range(1, 100):
    for y in range(9999 // x):
        if is_pan_mult(x, y):                
            cache.add(is_pan_mult(x, y))

print(sum(cache))






