##Euler 45
def x3(x):
   return int(x*(x+1)/2)

def x5(x):
   return int(x*(3*x-1)/2)

def x6(x):
   return x*(2*x-1)

limit = 60_000
while True:   
   set_x3 = {x3(x) for x in range(286, limit)}
   set_x5 = {x5(x) for x in range(166, limit)}
   set_x6 = {x6(x) for x in range(144, limit)}
   set_r = set.intersection(set_x3, set_x5, set_x6)
   if len(set_r) > 0:
      list_r = sorted([x for x in set_r])      
      result = list_r[0]
      break
   else:
      limit += 60_000
      
print(f'{result = }')

