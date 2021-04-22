import tkinter as tk
from tkinter import *
import des
import matplotlib.pyplot as plt

root = tk.Tk()
root.title('DES')
root.geometry('400x300')


def check(s):
	hexa=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	if len(s)==0 or len(s)%16!=0:
		return False
	for i in range(len(s)):
		print(s[i])
		if s[i] not in hexa:
			return False
	return True

diag = plt.figure(figsize=(3,3))

def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	print(INPUT)
	listing=[]
	if(check(INPUT)):
		Output1.delete('1.0',END)
		Output1.insert(END, 'Correct input')
		Output2.delete('1.0', END)
		Output2.insert(END, 'Correct input')
		Output3.delete('1.0', END)
		Output3.insert(END, 'Correct input')
		rounds = int(variable.get())
		global diag
		diag = des.des(rounds,listing)
		print(listing[0])
		print(listing[1])
		print(listing[2])
		Output1.delete('1.0',END)
		Output1.insert(END, listing[0])
		Output2.delete('1.0', END)
		Output2.insert(END, listing[1])
		Output3.delete('1.0', END)
		Output3.insert(END, listing[2])
	else:
		Output1.delete('1.0', END)
		Output1.insert(END, "Wrong input")
		Output2.delete('1.0', END)
		Output2.insert(END, "Wrong input")
		Output3.delete('1.0', END)
		Output3.insert(END, "Wrong input") 

l = Label(text = "Insert only hexadecimal input")
l0 = Label(text = '# of rounds')
inputtxt = Text(root, height = 6,
				width = 18,
				bg = "light yellow")
OPTIONS = [
1,4,8,16,32
]

def printing():
	diag.show()
	

variable = StringVar(root)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(root, variable, *OPTIONS)

Output1 = Text(root, height = 6, 
				width = 16, 
				bg = "light cyan")
l1 = Label(text = '64 bit block')
Output2 = Text(root, height = 6, 
				width = 16, 
				bg = "light cyan")
l2 = Label(text= '32 bit block')
Output3 = Text(root, height = 6, 
				width = 16, 
				bg = "light cyan")
l3 = Label(text= '16 bit block')
Display = Button(root, height = 2,
				width = 15, 
				text ="Execute",
				command = lambda:Take_input())
graph = Button(root, height = 1,
				width = 5, 
				text ="GRAPH",
				command = lambda:printing())


graph.place(x=50,y=50)
l.place(x=120,y=0)
l0.place(x=310,y=20)
inputtxt.place(x=140,y=20)
Display.place(x=140,y=125)
w.place(x=320,y=40)
Output1.place(x=5,y=170)
Output2.place(x=135, y=170)
Output3.place(x=270, y=170)
l1.place(x=20,y=280)
l2.place(x=160,y=280)
l3.place(x=290,y=280)

root.mainloop()