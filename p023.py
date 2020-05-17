##Euler 23

def sum_divs(n):
   '''function return sum proper divisors of number'''
   
   s = []
   for i in range(1, int(n**0.5)+2):
      if n%i == 0:
         s += [i, n/i]
   return sum(set(s)) - n


abundent_numbers = set()
summ = 0
for i in range(1, 28124):
   if sum_divs(i) > i:
      abundent_numbers.add(i)
   if not any((i-a in abundent_numbers) for a in abundent_numbers):
      summ += i
print(summ)






