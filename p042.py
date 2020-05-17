##Euler 42
import string

def alphabet():
   # create dic {char: position in alphabet}
   return {x:i for x, i in zip(string.ascii_lowercase, range(1, 100))}

def triangle_numbers(limit):
   #create set of triangle numbers
   return {int(1/2*n*(n+1)) for n in range(limit)}

def num_of_word(word, alphabet_dic):
   # sum(letters -> positions in alphabet) SKY = 19 + 11 + 25 = 55
   return sum([alphabet_dic[i] for i in word])

def read(file):
   #return list of words
   with open(file) as f:     
      return [w.lower() for w in f.read().strip('"').split('","')]
   
words = read('p042_words.txt')
alphabet_dic = alphabet()
triangle_set = triangle_numbers(1000)

summ = 0
for word in words:
   temp = num_of_word(word, alphabet_dic)
   if temp in triangle_set:
      summ += 1
print(f'{summ = }')

   
   
   














              
     




            
