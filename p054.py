##Euler 54
##Poker hands

from collections import Counter
import time

def is_royal_flush(x1, y1, x2, y2):
    if all(x in x1 for x in kdict)  and len(set(y1)) == 1:
        return 1
    if all(x in x2 for x in kdict) and len(set(y2)) == 1:
        return 2
    
def is_straight_flush(x1, y1, x2, y2):
    s1 = [kdict[x] for x in x1]
    if sum(s1)/5 == s1[2] and len(set(y1)) == 1:
        return 1
    s2 = [kdict[x] for x in x2]
    if sum(s2)/5 == s2[2] and len(set(y2)) == 1:
        return 2

def is_four_of_a_kind(x1, y1, x2, y2):
    c1 = (Counter(x1))
    c2 = (Counter(x2))
    if c1[list(c1)[0]] == 4 and c2[list(c2)[0]] == 4:
        return is_high_card(x1, y1, x2, y2)
    if c1[list(c1)[0]] == 4:
        return 1
    if c2[list(c2)[0]] == 4:
        return 2

def is_full_house(x1, y1, x2, y2): 
    if len(set(x1)) == 2 and len(set(x2)) ==2:
        return is_three_of_a_kind(x1, y1, x2, y2)
    if len(set(x1)) == 2:
        return 1
    if len(set(x2)) == 2:
        return 2

def is_flush(x1, y1, x2, y2):
    if len(set(y1)) == 1:
        return 1
    if len(set(y2)) == 1:
        return 2

def is_straight(x1, y1, x2, y2):
    s1 = [kdict[x] for x in x1]
    if sum(s1)/5 == s1[2]:
        return 1
    s2 = [kdict[x] for x in x2]
    if sum(s2)/5 == s2[2]:
        return 2

def is_three_of_a_kind(x1, y1, x2, y2):
    [kdict[x] for x in list(x1)]
    c1 = (Counter(x1))
    c2 = (Counter(x2))
    mc1 = c1.most_common()[0][0]
    mc2 = c2.most_common()[0][0]
    mcc1 = c1.most_common()[0][1]
    mcc2 = c2.most_common()[0][1]
    if mcc1 == mcc2 == 3:
        if mc1 > mc2:
            return 1
        if mc1 < mc2:
            return 2
    if mcc1 == 3:
        return 1
    if mcc2 == 3:
        return 2

def is_two_pairs(x1, y1, x2, y2):    
    if len(set(x1)) == 3 and len(set(x2)) == 3:
        c1 = Counter(x1)
        c2 = Counter(x2)
        s1 = dict(c1)
        s2 = dict(c2)
        print(s1, s2)
        r1 = [kdict[x] for x in s1 if s1[x]==2]
        r2 = [kdict[x] for x in s2 if s2[x]==2]
        print(r1, r2)
        if max(r1) > max(r2):
            return 1
        if max(r1) < max(r2):
            return 2
        if max(r1) == max(r2):
            return is_high_card(x1, y1, x2, y2)
    if len(set(x1)) == 3:
        return 1
    if len(set(x2)) == 3:
        return 2  

def is_one_pair(x1, y1, x2, y2):
    if len(set(x1)) == 4 and len(set(x2)) == 4:
        c1 = Counter(x1)
        c2 = Counter(x2)
        t1 = (c1.most_common()[0][0])
        t2 = (c2.most_common()[0][0])
        r1 = kdict[t1]
        r2 = kdict[t2]
        if r1 > r2:
            return 1
        if r1 < r2:
            return 2
        if r1 == r2:
            return is_high_card(x1, y1, x2, y2)
    if len(set(x1)) == 4:
        return 1
    if len(set(x2)) == 4:
        return 2 

def is_high_card(x1, y1, x2, y2):
    list_x1 = sorted([kdict[x] for x in list(x1)])
    list_x2 = sorted([kdict[x] for x in list(x2)])
    while True:
        for x in range(4, 0, -1):
            if list_x1[x] == list_x2[x]:
                continue
            if list_x1[x] > list_x2[x]:
                return 1
            if list_x1[x] < list_x2[x]:
                return 2   

def main():    
    with open('p054_poker.txt') as f:
        for line in f:
            t = line.split()
            x1 = ''.join([x[0] for x in t[:5]])
            y1 = ''.join([x[1] for x in t[:5]])
            x2 = ''.join([x[0] for x in t[5:10]])
            y2 = ''.join([x[1] for x in t[5:10]])
            r = []
            if r1 := is_royal_flush(x1, y1, x2, y2):
                r.append(r1)
            else:
                if r2 := is_straight_flush(x1, y1, x2, y2):
                    r.append(r2)
                else:
                    if r3 := is_four_of_a_kind(x1, y1, x2, y2):
                        r.append(r3)
                    else:                            
                        if r4 := is_full_house(x1, y1, x2, y2):
                            r.append(r4)
                        else:                            
                            if r5 := is_flush(x1, y1, x2, y2):
                                r.append(r5)
                            else:
                                if r6 := is_straight(x1, y1, x2, y2):
                                    r.append(r6)
                                else:
                                    if r7 := is_three_of_a_kind(x1, y1, x2, y2):
                                        r.append(r7)
                                    else:
                                        if r8 := is_two_pairs(x1, y1, x2, y2):
                                            r.append(r8)
                                        else:
                                            if r9 := is_one_pair(x1, y1, x2, y2):
                                                r.append(r9)
                                            else:
                                                if r10 := is_high_card(x1, y1, x2, y2):
                                                    r.append(r10)
            globalr.append(r[0])
            
start = time.time()            
kdict = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, \
         '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}            
globalr = []
main()
print(f'{Counter(globalr)[1]} in {time.time()-start}')




##        T = 10  #10
##        J = 11   #Valet
##        Q = 12  #Dama
##        K = 13  #Korol
##        A = 14  #Tuz
##        S = 1   #Piki
##        C = 1   #Trefy
##        H = 1   #Chervy
##        D = 1   #Bubny
    
   
##print(is_straight_flush('TJQK2', 'CCCCC', '23456', 'CCCCC'))
##print(is_four_of_a_kind('22223', 'CCCCC', '23456', 'CCCCC'))
##print(is_full_house('22555', 'HDCDH', '33399', 'CHSSD'))
##print(is_flush('22444', 'HHHHH', '33392', 'CDSSD'))
##print(is_straight('TJQK2', 'CCCDC', '89TJQ', 'CHCDC'))
##print(is_three_of_a_kind('QQ444', 'CCCDC', '88TJ8', 'CHCDC'))
##print(is_two_pairs('KAK77', 'DDHHS', '55529', 'DHSDC'))
##print(is_one_pair('TJTK7', 'CCCDC', 'T9TJ8', 'CHCDC'))
##print(is_high_card('TJ3KA', 'CCCDC', 'A9TJQ', 'CHCDC'))

##KD AD KH 7H 7S 5D 5H 5S 2D 9C
##['8C', 'TS', 'KC', '9H', '4S', '7D', '2S', '5D', '3S', 'AC']   
