import tkinter as tk
from tkinter import *
import time
root = Tk()
root.title('TicTacToe')
list=[]


def result(x):
	global count
	count=0
	if x==1:
		text='First Won!!!'
	elif x==0:
		text = 'Second Won!!!'
	else : 
		text = 'Draw!!!'
	win = tk.Toplevel()
	win.wm_title("Result")
	ans = Label(win,text=text)
	ans.pack()
	for i in range(9):
		list[i].configure(text='')





def check():
	mist=[]
	for i in range(9):
		mist.append(list[i]['text'])
	if (mist[0]==mist[1] and mist[0]==mist[2]):
		if mist[0]=='O':
			print('first won')
			result(1)
		elif mist[0]=='X':
			print('second won')
			result(0)
	elif(mist[3]==mist[4] and mist[3]==mist[5]):
		if mist[3]=='O':
			print('first won')
			result(1)
		elif mist[3]=='X':
			print('second won')
			result(0)
	elif(mist[6]==mist[7] and mist[6]==mist[8]):
		if mist[6]=='O':
			print('first won')
			result(1)
		elif mist[6]=='X': 
			print('second won')
			result(0)
	elif(mist[0]==mist[4] and mist[0]==mist[8]):
		if mist[0]=='O':
			print('first won')
			result(1)
		elif mist[0]=='X':
			print('second won')
			result(0)
	elif(mist[6]==mist[4] and mist[6]==mist[2]):
		if mist[4]=='O':
			print('first won')
			result(1)
		elif mist[4]=='X':
			print('second won')
			result(0)
	elif(mist[0]==mist[3] and mist[0]==mist[6]):
		if mist[0]=='0':
			print('first won')
			result(1)
		elif mist[0]=='X':
			print('second won')
			result(0)
	elif(mist[1]==mist[4] and mist[1]==mist[7]):
		if mist[1]=='O':
			print('first won')
			result(1)
		elif mist[1]=='X':
			print('second won')
			result(0)
	elif(mist[2]==mist[5] and mist[2]==mist[8]):
		if mist[2]=='O':
			print('first won')
			result(1)
		elif mist[2]=='X':
			print('second won')
			result(0)
	else:
		flag=False
		for i in range(9):
			if mist[i]=='':
				flag=True
		if flag==False:
			print('Draw')
			result(9)





count=0
def fill(x):
	global count
	if count%2==0:
		if list[x].cget('text')=='X':
			count-=1
		else:
			list[x].configure(text='O')
	else:
		if list[x].cget('text')=='O':
			count-=1
		else:
			list[x].configure(text='X')
	count+=1
	check()

for i in range(9):
	list.append(Button(root,width=1,height=1,text=''))
	list[i].grid(row=int(i/3),column=i%3,sticky='news')
	root.rowconfigure(i%3,weight=1)
	root.columnconfigure(i%3,weight=1)

list[0].configure(command = lambda : fill(0))
list[1].configure(command = lambda : fill(1))
list[2].configure(command = lambda : fill(2))
list[3].configure(command = lambda : fill(3))
list[4].configure(command = lambda : fill(4))
list[5].configure(command = lambda : fill(5))
list[6].configure(command = lambda : fill(6))
list[7].configure(command = lambda : fill(7))
list[8].configure(command = lambda : fill(8))


root.mainloop()