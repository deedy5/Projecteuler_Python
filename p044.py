##Euler 44
pentagon_numbers = [int(n*(3*n - 1)/2) for n in range(1, 10000)]

pn_set = set(pentagon_numbers)

d_min_yx = 9999999999999999
for x in pentagon_numbers:
   for y in pentagon_numbers:
      if (x + y) in pn_set and (y - x) in pn_set:
         if abs(y - x) < d_min_yx:
            d_min_yx = abs(y - x)

print(d_min_yx)


