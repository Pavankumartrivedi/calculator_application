
from tkinter import *
from math import *

def btnClick(numbers):
    global operator
    operator = operator +  str(numbers)
    text_input.set(operator)
    

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator


    sumup = str(eval(operator))
    text_input.set(sumup)
    operator =""
def btnquit():
    global  operator
    operator = quit()

cal = Tk()
cal.title("Calculator")
operator = ""
text_input = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'), textvariable = text_input, bd = 30, insertwidth = 4, bg = "powder blue", justify = 'right').grid(columnspan = 4)

btn7 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "7" ,bg = "purple",command = lambda : btnClick(7)).grid(row = 1,column =0)
btn8 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "8" ,bg = "purple",command = lambda : btnClick(8)).grid(row = 1,column =1)
btn9 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "9", bg = "purple",command = lambda : btnClick(9)).grid(row = 1,column =2)
Addition = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "+" ,bg = "purple",command = lambda : btnClick("+")).grid(row = 1,column =3)
#========================================================================================================================================

btn4 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "4" ,bg = "purple",command = lambda : btnClick(4)).grid(row = 2,column =0)
btn5 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "5" ,bg = "purple",command = lambda : btnClick(5)).grid(row = 2,column =1)
btn6 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "6" ,bg = "purple",command = lambda : btnClick(6)).grid(row = 2,column =2)
Subtraction = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "-", bg = "purple",command = lambda : btnClick("-")).grid(row = 2,column =3)
#========================================================================================================================================

btn1 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "1" ,bg = "purple",command = lambda : btnClick(1)).grid(row = 3,column =0)
btn2 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "2" ,bg = "purple",command = lambda : btnClick(2)).grid(row = 3,column =1)
btn3 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "3" ,bg = "purple",command = lambda : btnClick(3)).grid(row = 3,column =2)
Multiplication= Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "*", bg = "purple",command = lambda : btnClick("*")).grid(row = 3,column =3)
#========================================================================================================================================

btn0 = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "0" ,bg = "purple",command = lambda : btnClick(0)).grid(row = 4,column =0)
btnClear = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "C" ,bg = "purple" , command =btnClearDisplay).grid(row = 4,column =1)
btnEquals = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "=" ,bg = "purple" , command = btnEqualsInput).grid(row = 5,column =3)
division = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "/", bg = "purple",command = lambda : btnClick("/")).grid(row = 4,column =3)
#===================================================================================================================================================================================
btnquit = Button(cal,padx = 16,bd = 15 ,fg = "black",font =('arial',20,'bold'),text = "x" ,bg = "purple",command = btnquit).grid(row = 5,column =0)
#======================================================================================================================================================================================
Square_Root   = Button(cal,padx = 16,bd = 15 ,fg = "black",font =('arial',20,'bold'),text = "√" ,bg = "purple",command = lambda  : btnClick("**.5")).grid(row = 5,column =1)
percentage = Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "%", bg = "purple",command = lambda : btnClick("1/100")).grid(row = 5,column =2)
pie= Button(cal,padx = 16,bd = 8 ,fg = "black",font =('arial',20,'bold'),text = "π", bg = "purple",command = lambda : btnClick("*3.14")).grid(row = 4,column =2)
#===============================================================================================================================================================================================

cal.mainloop()
