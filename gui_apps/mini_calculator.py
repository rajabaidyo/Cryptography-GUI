from tkinter import *

root = Tk()
root.title('mini-calculator')

inp=Text(root,width=12,height=1)
inp.grid(row=0,column=0,columnspan=2,sticky='news')
out=Text(root,width=12,height=1)
out.grid(row=1,column=0,columnspan=2,sticky='news')

def backspace():
    input = inp.get("1.0", "end-1c") 
    inp.delete('1.0', END)
    inp.insert(END,input[0:-1])
def calculate():
    input = inp.get("1.0", "end-1c")
    try:
        ans = eval(input)
        out.delete('1.0',END)
        out.insert(END, ans)
    except:
        out.delete('1.0', END)
        out.insert(END, 'check input')


zero = Button(root,text='0',command=lambda : inp.insert(END, '0'))
lbrac = Button(root,text='(',command=lambda : inp.insert(END, '('))
rbrac = Button(root,text=')',command=lambda : inp.insert(END, ')'))
one = Button(root,text='1',command=lambda : inp.insert(END, '1'))
two = Button(root,text='2',command=lambda : inp.insert(END, '2'))
three = Button(root,text='3',command=lambda : inp.insert(END, '3'))
four = Button(root,text='4',command=lambda : inp.insert(END, '4'))
five = Button(root,text='5',command=lambda : inp.insert(END, '5'))
six = Button(root,text='6',command=lambda : inp.insert(END, '6'))
seven = Button(root,text='7',command = lambda : inp.insert(END, '7'))
eight = Button(root,text='8',command = lambda : inp.insert(END, '8'))
nine = Button(root,text='9',command = lambda : inp.insert(END, '9'))
plus = Button(root,text='+',command=lambda : inp.insert(END, '+'))
minus = Button(root,text='-',command= lambda : inp.insert(END, '-'))
multi = Button(root,text='*',command=lambda : inp.insert(END, '*'))
div =Button(root,text='/',command = lambda : inp.insert(END, '/'))
perc = Button(root,text='%',command = lambda : inp.insert(END, '/100'))
back = Button(root,text='<=',command = lambda: backspace())
clear = Button(root,text='AC',command = lambda : inp.delete('1.0', END))
equal = Button(root,text='=',command = lambda : calculate())




#placing the keys 
clear.grid(row=0,column=2,sticky='news')
equal.grid(row=0,column=3,sticky='news')
back.grid(row=1,column=2,sticky='news')
perc.grid(row=1,column=3,sticky='news')
zero.grid(row=2,column=0,sticky='news')
lbrac.grid(row=2,column=1,sticky='news')
rbrac.grid(row=2,column=2,sticky='news')
div.grid(row=2,column=3,sticky='news')
one.grid(row=3,column=0,sticky='news')
two.grid(row=3,column=1,sticky='news')
three.grid(row=3,column=2,sticky='news')
multi.grid(row=3,column=3,sticky='news')
four.grid(row=4,column=0,sticky='news')
five.grid(row=4,column=1,sticky='news')
six.grid(row=4,column=2,sticky='news')
minus.grid(row=4,column=3,sticky='news')
seven.grid(row=5,column=0,sticky='news')
eight.grid(row=5,column=1,sticky='news')
nine.grid(row=5,column=2,sticky='news')
plus.grid(row=5,column=3,sticky='news')

for i in range(4):
    root.columnconfigure(i,weight=1)
for i in range(6):
    root.rowconfigure(i,weight=1)


root.mainloop()