##Euler 17
dic = {n:0 for n in range(0,1001)}

dic[0] = 0#''
dic[1] = 3#'one'
dic[2] = 3#'two'
dic[3] = 5#'three'
dic[4] = 4#'four'
dic[5] = 4#'five'
dic[6] = 3#'six'
dic[7] = 5#'seven'
dic[8] = 5#'eight'
dic[9] = 4#'nine'
dic[10] = 3#'ten'
dic[11] = 6#'eleven'
dic[12] = 6#'twelve'
dic[13] = 8#'thirteen'
dic[14] = 8#'fourteen'
dic[15] = 7#'fifteen'
dic[16] = 7#'sixteen'
dic[17] = 9#'seventeen'
dic[18] = 8#'eighteen'
dic[19] = 8#'nineteen'
dic[20] = 6#'twenty'
dic[30] = 6#'thirty'
dic[40] = 5#'forty'
dic[50] = 5#'fifty'
dic[60] = 5#'sixty'
dic[70] = 7#'seventy'
dic[80] = 6#'eighty'
dic[90] = 6#'ninety'

#for loop to generate the values for 21-99
#as we have already entered the values under
#20 manually
for i in range(21,100):
	tens = int(i/10)*10
	ones = i - tens
	dic[i]  = dic[tens]+dic[ones]

#for loop to generate values for 100-999
for i in range(100,1000):
	hundreds = int(i/100)
	tens_ones = i - hundreds*100
	#if the value of tens and ones place is 0
	#just use 'hundred' instead of 'and hundred'
	if tens_ones == 0:
		dic[i] = dic[hundreds] + 7#'hundred'
	else:
		#10 refers - 'and hundred'
		dic[i] = dic[hundreds] +10+dic[tens_ones]

dic[1000] = 11#'one thousand'

#printing the value of each letter digit sum
print(sum(dic.values()))


