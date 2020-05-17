##Euler 21
def div_sum(number):    
    return sum([n for n in range(1, int(number*0.5+1)) if number%n==0]) 

def ami_number(n):
    if n == div_sum(div_sum(n)) and n != div_sum(n):
        return n
    else:
        return False             

print(sum([i for i in range(10000) if i==div_sum(div_sum(i)) and i!=div_sum(i)]))       


