##Euler 12

def triang_number_divisions(divisions):
    n = 0
    i = 0    
    while True:
        i+=1
        n += i
        count = 0
        c = int(n**0.5+1)
        for j in range(1, c):
            if n % j == 0:        
                count += 2           
                if count == divisions:
                    return n
start = time.time()
print(triang_number_divisions(500))

####V2
##from concurrent.futures import ProcessPoolExecutor           
##def is_divisions(number):    
##    count = 0
##    c = int(number**0.5+1)
##    for j in range(1, c):
##        if number % j == 0:
##            count += 2
##            if count == 500:
##                return number
##               
##
##number_list = []
##n = 0
##for i in range(100000):
##    n += i
##    number_list.append(n)
##
##def comp():
##    with ProcessPoolExecutor(4) as executor:
##        
##        future = executor.map(is_divisions, number_list)
##        print(future.result())
##        
##        
##
##if __name__ == '__main__':

##    comp()





    
