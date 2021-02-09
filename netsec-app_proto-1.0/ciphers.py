import string 

#done
#caesar cipher
def caesar_e(input,key):
	if len(key)>1:
		print('key error')
		return 'key error'
	elif len(key) == 0:
		print('no key provided')
		return 'no key provided'
	ans=""
	for val in input :
		if val in string.ascii_lowercase:
		 	ans = ans + (chr ((ord(val)-97+ord(key)-96)%26 + 97) )
		elif val in string.ascii_uppercase:
			ans = ans + (chr ((ord(val)-65+ord(key)-96)%26 + 65) )
		else:
			ans = ans + val
	return ans

def caesar_d(input,key):
	if len(key)>1:
		print('key error')
		return 'key error'
	elif len(key) == 0:
		print('no key provided')
		return 'no key provided'
	ans=""
	for val in input :
		if val in string.ascii_lowercase:
		 	ans = ans + (chr ((ord(val)-97-ord(key)+96)%26 + 97) )
		elif val in string.ascii_uppercase:
			ans = ans + (chr ((ord(val)-65-ord(key)+96)%26 + 65) )
		else:
			ans = ans + val
	return ans













#monoalphabetic cipher
def monoalpha_e(input,list):
	# print(list)
	ans=""
	for each in input:
		if each in string.ascii_lowercase:
			ans = ans+list[each]
		else:
			ans=ans+each
	return ans
	# return 'monoalphabetic encryption'

def monoalpha_d(input,list):
	rev_list={}
	#making the reverse mapping list
	for i in range(26):
		rev_list[list[chr(97+i)]]=chr(97+i)
	ans=""
	for each in input:
		if each in string.ascii_lowercase:
			ans = ans+rev_list[each]
		else:
			ans=ans+each
	return ans













#done
#simmons cipher - same function for encryption and decryption 
def simmons_e(input):
	ans = ""
	for val in input:
		if val in string.ascii_lowercase:
			ans=ans+chr(122-ord(val)+97)
		elif val in string.ascii_uppercase:
			ans=ans+chr(90-ord(val)+65)
		else:
			ans=ans+val
	return ans










def filling(first,second,list,flag):
	print(first+second)
	# print(list[first])
	temp = -1 if flag==1 else 1
	# print(list[second])
	if list[first][0]==list[second][0] and list[first][1]!=list[second][1]:
		return (list[ list[first][0] + str( (int(list[first][1]) + temp)%5) ]+list[list[second][0] + str( (int(list[second][1]) + temp)%5)] )
	elif list[first][1]==list[second][1] and list[first][0]!=list[second][0]:
		return (list[str( (int(list[first][0]) + temp)%5 ) + list[first][1]]+list[str( (int(list[second][0]) + temp)%5) + list[second][1] ] )
	elif first==second:
		return (first+first)
	else:
		return (list[list[first][0]+list[second][1]] + list[list[second][0]+list[first][1]])


#playfair cipher
def playfair_e(input,key,leftout,char_filler,flag):
	#making the encryption - decryption matrix
	seq = 'abcdefghijklmnopqrstuvwxyz'
	list = {}
	row = 0
	col =0 
	for i in key:
		list[i]=(str(row)+str(col))
		list[str(row)+str(col)]=i
		col=col+1
		if col == 5 :
			row = row+1
			col=0
	check = key + leftout
	for i in seq :
		if i not in check:
			list[i]=(str(row)+str(col))
			list[str(row)+str(col)]=i
			col=col+1
			if col==5:
				row=row+1
				col=0
	print(list)

	# encryption - decryption matrix
	for i in range(5):
		for j in range(5):
			print(list[str(i)+str(j)], end = " ")
			print(list[list[str(i)+str(j)]],end = " ")
		print('\n')


	#writing the driver code
	ans = ""
	i = 0
	while(i<len(input)):
		first = input[i]
		print(type(first))
		if first == leftout:
			first = char(char_filler)
		if first in string.ascii_lowercase:
			if i == len(input)-1:
				second = char_filler
			else:
				second = input[i+1]
		else:
			ans = ans + first
			i=i+1
			continue
		if second == leftout:
			second = char_filler
		if second in string.ascii_lowercase:
			ans = ans+ filling(first,second,list,flag)
		else : 
			ans = ans + filling(first,char_filler,list,flag) + second
		i+=2

	return ans










#Hill cipher
def hill_e():
	return 'hill encryption'

def hill_d():
	return 'comming soon! \nisko code karne main coder ki phat gyi!'












#done
#Vigenere cipher
def vigenere_e(input,mainkey):
	if len(mainkey)==0:
		print('key error')
		return 'key error'
	ans = ""
	count=0
	for val in input:
		key = mainkey[count]
		count = (count+1)%len(mainkey)
		if val in string.ascii_lowercase:
			ans = ans + chr((ord(val)-97+ord(key)-96)%26 + 97)
		elif val in string.ascii_uppercase:
			ans = ans + chr ((ord(val)-65+ord(key)-96)%26 + 65)
		else:
			ans = ans + val
	return ans

def vigenere_d(input,mainkey):
	if len(mainkey)==0:
		print('key error')
		return 'key error'
	ans = ""
	count = 0
	for val in input :
		key = mainkey[count]
		count = (count+1)%len(mainkey) 
		if val in string.ascii_lowercase:
			ans = ans + chr((ord(val)-97 - ord(key)+96)%26+97)
		elif val in string.ascii_uppercase:
			ans = ans + chr((ord(val)-65-ord(key)+96)%26+65)
		else:
			ans = ans + val
	return ans