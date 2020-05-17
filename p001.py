import time

def sum_kratn_3_5(diapason):
    summ = 0
    for i in range(int(diapason)):
        if i % 3 == 0 or i % 5 == 0:
            summ = summ + i
            print(summ)
    return summ

print("Enter diapason: ")
diapason = input()
start_time = time.time()
print(f"summa ravna {sum_kratn_3_5(diapason)}")
print("--- %s seconds ---" % (time.time() - start_time))
