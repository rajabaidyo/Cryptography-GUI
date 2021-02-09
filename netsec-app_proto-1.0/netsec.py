import tkinter as tk
from tkinter import *
import datetime
import ciphers
import re 
import string 
from collections import OrderedDict

class display():

	def __init__(self):
		self.var = IntVar()
		self.R1 = Radiobutton(self, text="Press if inp = cipher-txt", variable=self.var, value=1)
		self.R1.place(x=0,y=60)

		self.inputtxt = Text(self, height = 7, 
						width = 20, 
						bg = "light yellow") 
		self.inputtxt.place(x=10,y=100)

		self.encrypt = Button(self,text='Encrypt',command = None)
		self.encrypt.place(x=270,y=50)

		self.Output = Text(self, height = 7, 
					width = 20, 
					bg = "light cyan") 
		self.Output.place(x=225,y=100)

		

	def extra_key(self):
		self.key_name = Label(self, text = 'Key')
		self.key_name.place(x=120,y=230)
		self.key = Entry(self,textvariable = 'key', relief = 'sunken', width = 10)
		self.key.place(x=160,y=230)

	def extra_play(self):
		self.submit = Button(self, text = 'submit', command = None,height = 0, width = 5, bd ='5',padx = 1,pady=0)
		self.submit.place(x=250,y=230)

	def leftnfill(self):
		self.lolab = Label(self,text = 'leftout \nneeded')
		self.fclab = Label(self,text = 'filler chr\nneeded')
		self.left = Entry(self,textvariable = 'left', relief = 'sunken',width = 5)
		self.fill = Entry(self,textvariable = 'fill', relief = 'sunken', width = 5)
		self.left.place(x=80,y=270)
		self.fill.place(x=300,y=270)
		self.lolab.place(x=20,y=260)
		self.fclab.place(x=240,y=260)

	def mono_map(self):
		self.cell = []
		self.mell = []
		self.submit = Button(self,text='submit',command = None, bd=1, padx=0,pady=1)
		self.submit.place(x=175,y=200)
		for i in range(13):
			first = chr(97+i)
			second = chr(97+i+13)
			#print(first, second)
			first_map = first+'map'
			second_map = second+'map'
			self.first = Label(self,text = first)
			self.second = Label(self, text = second)
			self.first_map = Entry(self,textvariable=first_map,width=1)
			self.first_map.insert(0,first)
			self.second_map = Entry(self,textvariable=second_map,width=1)
			self.second_map.insert(0,second)
			self.cell.append(self.first_map)
			self.mell.append(self.second_map)
			self.first_map.place(x=10+(30*i),y=240)
			self.second_map.place(x=10+(30*i),y=270)
			self.first.place(x=(30*i), y = 240)
			self.second.place(x=(30*i), y = 270)
		self.cell.extend(self.mell)
		self.mell.clear()

	def hill_mat(self):
		self.one = Entry(self,textvariable = 'one',width = 2)
		self.two = Entry(self,textvariable = 'two',width = 2)
		self.three = Entry(self,textvariable = 'three',width = 2)
		self.four = Entry(self,textvariable = 'four',width = 2)
		self.one.place(x=180,y=240)
		self.two.place(x=200,y=240)
		self.three.place(x=180,y=260)
		self.four.place(x=200,y=260)
		self.key_name = Label(self, text = 'Key')
		self.key_name.place(x=140,y=250)
		self.check = Button(self,text = 'check_key',command = None,bd = 3, padx = 1,pady =1)
		self.check.place(x=235,y=245)

			



class netsec(tk.Tk):
	def __init__(self,*args, **kwargs):
		tk.Tk.__init__(self,*args,**kwargs)
		self.title('Netsec-app')
		self.geometry('400x300')
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		self.frames = {}

		for each in (home,caesar,monoalpha,simmons,playfair,hill,vigenere):
			frame = each(container,self)
			frame.grid(row=0,column=0,sticky='nsew')
			self.frames[each] = frame

		self.show_frame(home)


	def show_frame(self,page_num):
		frame=self.frames[page_num]
		frame.tkraise()


	def menus(self):
		menu = Menu(self)

		item = Menu(menu)
		about = Menu(menu)
		

		menu.add_cascade(label='Ciphers', menu=item)
		item.add_command(label='Home',command= lambda:self.show_frame(home))
		item.add_command(label='Simmons',command = lambda:self.show_frame(simmons))
		item.add_command(label='Caesar',command = lambda: self.show_frame(caesar))
		item.add_command(label='Monoalpha',command = lambda:self.show_frame(monoalpha))
		item.add_command(label='Playfair',command = lambda:self.show_frame(playfair))
		item.add_command(label='Hill',command = lambda:self.show_frame(hill))
		item.add_command(label='Vigenere',command = lambda:self.show_frame(vigenere))

		menu.add_cascade(label='About', menu = about)
		about.add_command(label='About_app', command=None)
		about.add_command(label='Demo', command=None)
		about.add_command(label='Exit',command = self.destroy)


		self.config(menu=menu)
		

class home(tk.Frame, display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()
		

		lbl = Label(self,text = 'Home');
		lbl.pack()


class caesar(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)
		display.extra_key(self)

		lbl = Label(self,text = 'Caesar Cipher');
		lbl.pack()
		self.encrypt.config(command = lambda : self.split())

	def split(self):
		if self.var.get()==0:
			self.encryption()
		else:
			self.decryption()

	def encryption(self):
		input = self.inputtxt.get("1.0", "end-1c")
		key = self.key.get()
		# print(key)
		#print(input)
		self.Output.delete('1.0', END)
		self.Output.insert(END,ciphers.caesar_e(input,key))
	
	def decryption(self):
		self.var.set(0)
		input = self.inputtxt.get("1.0", "end-1c")
		key = self.key.get()
		self.Output.delete('1.0', END)
		self.Output.insert(END, ciphers.caesar_d(input,key))


class monoalpha(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)
		display.mono_map(self)

		lbl = Label(self,text = 'Monoalphabetic ciphers');
		lbl.pack()
		self.encrypt.config(command = lambda : self.split())
		self.submit.config(command = lambda: self.key_check())
		self.inputtxt.insert(END,'enter unique mapping for each character\npress submit to check the mapping')

	def key_check(self):
		self.list={}
		flag = True
		for i in range(26):
			print(self.cell[i].get())
		for i in range(26):
			tempo =  self.cell[i].get()
			if tempo in self.list.values() or len(tempo)!=1 or tempo==None or tempo not in string.ascii_lowercase:
				flag = False
				self.inputtxt.delete('1.0',END)
				self.inputtxt.insert(END,'enter unique mapping for each character\npress submit to check the mapping')
				self.Output.delete('1.0',END)
				self.Output.insert(END,'maulitple instances of same mapped value/uppercase fournd/empty space etc.')
				'''for j in range(26):
					self.cell[j].delete(0,'end')'''
				self.list.clear()
				break
			else:
				self.list[chr(97+i)]=tempo
		if flag==True:
			self.Output.delete('1.0',END)
			self.inputtxt.delete('1.0',END)
			self.Output.insert(END,'mapping is fine!\nenter input and press encypt')



	def split(self):
		if self.var.get()==0:
			self.encryption()
		else:
			self.decryption()

	def encryption(self):
		# print(self.list)
		input = self.inputtxt.get("1.0", "end-1c")
		print(input)
		self.Output.delete('1.0',END)
		self.Output.insert(END,ciphers.monoalpha_e(input,self.list))
	
	def decryption(self):
		input = self.inputtxt.get("1.0", "end-1c")
		self.var.set(0)
		self.Output.delete('1.0', END)
		self.Output.insert(END,ciphers.monoalpha_d(input,self.list))		

		# for i in range(7):
		# 	exec('btn'+str(i)+'.grid(row ='+ str(i%2+1)+',column = '+str(i+((i)%2+1)+1)+')')

class simmons(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)

		lbl = Label(self,text = 'Simmons');
		lbl.pack()
		self.encrypt.config(command = lambda : self.encryption())

	def encryption(self):
		input = self.inputtxt.get("1.0", "end-1c")
		print(input)
		self.Output.delete('1.0',END)
		self.Output.insert(END,ciphers.simmons_e(input))

class playfair(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)
		display.extra_key(self)
		display.extra_play(self)
		display.leftnfill(self)
		self.inputtxt.insert(END,"enter key,leftout and filler character & check compatability by pressing submit\n*lefout and filler char shouldn't be in the key")

		lbl = Label(self,text = 'Playfair cipher');
		lbl.pack()
		self.encrypt.config(command = lambda : self.split())
		self.submit.config(command = lambda: self.param_check())

	def removeDupWithOrder(self,str):  
		return "".join(OrderedDict.fromkeys(str)) 

	def param_check(self):
		key = self.key.get()
		lo =  self.left.get()
		cf = self.fill.get()
		if len(lo)==1 and len(cf)==1 and lo!=cf and key!=None and (lo or cf) not in key :
			self.Output.delete('1.0',END)
			self.inputtxt.delete('1.0',END)
			self.Output.insert(END,'key,leftout char and filler char are good\nEnter input and press encrypt now!!!')
		else:
			self.Output.delete('1.0',END)
			self.Output.insert(END,'pls follow the instructions on left')
			self.left.delete(0,'end')
			self.fill.delete(0,'end')
		


	def split(self):
		key = self.key.get()
		key = self.removeDupWithOrder(key)
		print(key)
		lo = self.left.get()
		cf = self.fill.get()
		if self.var.get()==0:
			self.encryption(key,lo,cf)
		else:
			self.decryption(key,lo,cf)

	def encryption(self,key,lo,cf):
		input = self.inputtxt.get("1.0", "end-1c")
		print(input)
		self.Output.delete('1.0',END)
		self.Output.insert(END,ciphers.playfair_e(input,key,lo,cf,0))
	
	def decryption(self,key,lo,cf):
		input = self.inputtxt.get("1.0", "end-1c")
		self.var.set(0)
		self.Output.delete('1.0', END)
		self.Output.insert(END, ciphers.playfair_e(input,key,lo,cf,1))

		# for i in range(7):
		# 	exec('btn'+str(i)+'.grid(row ='+ str(i%2+1)+',column = '+str(i+((i)%2+1)+1)+')')

class hill(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)
		display.hill_mat(self)

		lbl = Label(self,text = 'Hill cipher');
		lbl.pack()
		self.encrypt.config(command = lambda : self.split())

	def split(self):
		if self.var.get()==0:
			self.encryption()
		else:
			self.decryption()

	def encryption(self):
		input = self.inputtxt.get("1.0", "end-1c")
		print(input)
		self.Output.delete('1.0',END)
		self.Output.insert(END,ciphers.hill_e())
	
	def decryption(self):
		self.var.set(0)
		self.Output.delete('1.0', END) 
		self.Output.insert(END, ciphers.hill_d())

		# for i in range(7):
		# 	exec('btn'+str(i)+'.grid(row ='+ str(i%2+1)+',column = '+str(i+((i)%2+1)+1)+')')

class vigenere(tk.Frame,display):
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		controller.menus()

		display.__init__(self)
		display.extra_key(self)

		lbl = Label(self,text = 'Vigenere cipher');
		lbl.pack()
		self.encrypt.config(command = lambda : self.split())

	def split(self):
		if self.var.get()==0:
			self.encryption()
		else:
			self.decryption()

	def encryption(self):
		input = self.inputtxt.get("1.0", "end-1c")
		key = self.key.get()
		self.Output.delete('1.0', END)
		self.Output.insert(END, ciphers.vigenere_e(input,key))
	
	def decryption(self):
		self.var.set(0)
		input = self.inputtxt.get("1.0","end-1c")
		key = self.key.get()
		self.Output.delete('1.0', END)
		self.Output.insert(END, ciphers.vigenere_d(input,key))

		# for i in range(7):
		# 	exec('btn'+str(i)+'.grid(row ='+ str(i%2+1)+',column = '+str(i+((i)%2+1)+1)+')')



















app = netsec()
app.mainloop()


