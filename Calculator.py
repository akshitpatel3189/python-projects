from tkinter import *

ex = ''

def press(num): 
    global ex 
    ex = ex + str(num)
    equation.set(ex) 
  
def equalpress(): 
    try: 
        global ex 
        total = str(eval(ex)) 
        equation.set(total) 
        ex = '' 

    except:
        equation.set(' Arithmetic Error ')
        ex = '' 
  
def clearall():
    global ex 
    ex = '' 
    equation.set('0')

root = Tk()
root.geometry('355x475')
root.configure(bg='white')
root.title('Calculator')
root.iconbitmap('c.ico')
root.resizable(False,False)
  
button_frame = Frame(root,bg='#bfbfbf')
button_frame.pack()

equation = StringVar()
equation.set('0')
    
expression_field = Entry(button_frame,textvariable=equation,justify='right',
                                 font = ('arial',20,'bold'))
    
button1 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 1 ',bd=3,relief='raised',
                fg='black', bg='white',command=lambda: press(1), height=3, width=8) 
 
button2 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 2 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(2), height=3, width=8) 
  
button3 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 3 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(3), height=3, width=8) 

plus = Button(button_frame,font= ('times new roman',13,'bold'),text=' + ',bd=3,relief='raised',
              fg='yellow', bg='#4d4d4d',command=lambda: press("+"), height=3, width=8) 
  
button4 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 4 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(4), height=3, width=8) 

button5 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 5 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(5), height=3, width=8) 
  
button6 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 6 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(6), height=3, width=8) 

minus = Button(button_frame,font= ('times new roman',13,'bold'),text=' - ',bd=3,relief='raised',
               fg='yellow', bg='#4d4d4d',command=lambda: press("-"), height=3, width=8) 
  
button7 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 7 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(7), height=3, width=8) 
  
button8 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 8 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(8), height=3, width=8) 
  
button9 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 9 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(9), height=3, width=8) 

multiply = Button(button_frame,font= ('times new roman',13,'bold'),text=' * ',bd=3,relief='raised',
                  fg='yellow', bg='#4d4d4d',command=lambda: press("*"), height=3, width=8) 
  
button0 = Button(button_frame,font= ('times new roman',12,'bold'),text=' 0 ',bd=3,relief='raised',
                 fg='black', bg='white',command=lambda: press(0), height=3, width=8) 

decimal= Button(button_frame,font= ('times new roman',13,'bold'),text='.',bd=3,relief='raised',
                fg='yellow', bg='#4d4d4d',command=lambda: press('.'), height=3, width=8) 

clear = Button(button_frame,font= ('times new roman',12,'bold'),text='C',bd=3,relief='raised',
               fg='red', bg='white',command=clearall, height=3, width=8) 
  
divide = Button(button_frame,font= ('times new roman',13),text=' / ',bd=3,relief='raised',
                fg='yellow', bg='#4d4d4d',command=lambda: press("/"), height=3, width=8) 

equal = Button(button_frame,font= ('times new roman',13,'bold'),text=' = ',bd=3,relief='raised',
               fg='yellow', bg='#4d4d4d',command=equalpress,height=3)

mod = Button(button_frame,font= ('times new roman',13,'bold'),text=' % ',bd=3,relief='raised',
               fg='yellow', bg='#4d4d4d',command=lambda: press('%'), height=3, width=8)

expression_field.grid(row=0,column=0,columnspan = 4,ipadx=8,ipady=25,pady=15)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
minus.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

button0.grid(row=4, column=0)
decimal.grid(row=4, column=1)
mod.grid(row=4, column=2)
divide.grid(row=4, column=3)

equal.grid(row=5, column=0,columnspan = 2,sticky='nsew')
clear.grid(row=5, column=2,columnspan = 2,sticky='nsew')

root.mainloop()
