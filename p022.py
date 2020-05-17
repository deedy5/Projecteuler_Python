##Euler 22
def alphabet_value_of_name(name):
   return sum([alphabet_num[i] for i in name.lower()])

with open('p022_names.txt') as f:
    names = [name.lower() for name in f.read().strip('"').split('","')]

names_sorted = sorted(names)
names_sorted_num = {names_sorted[i]:i+1 for i in range(len(names))}

alphabet = list(map(chr, range(ord('a'), ord('z')+1)))
alphabet_num = {alphabet[i]: i+1 for i in range(len(alphabet))}

print(sum([alphabet_value_of_name(i)*names_sorted_num[i] for i in names_sorted]))





