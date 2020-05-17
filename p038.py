##Euler 38

max_num = 0
for n in range(1, 99999):
    temp_list = []
    for j in range(1, 10):
        temp_list.append(str(n*j))
        if len(temp_list) >= 10:
            break
        temp_n = ''.join(temp_list)
        if len(temp_n) >= 10:
            break
        if len(temp_n) == 9 and '0' not in temp_n:
            if ''.join(sorted(temp_n)) == '123456789':
                if int(temp_n) > int(max_num):
                    max_num = temp_n

print(max_num)
     
        
    




















              
##print(f'S{result} in {time.time() - start} sec.')       




            
