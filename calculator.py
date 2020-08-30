from tkinter import *

def actions(task):
    global flag
    
    temp = '0'
    
    if flag:
        temp = inp.get()
        inp.delete(0, END)
        flag = False
    
    if inp.get() == '0':
        inp.delete(0, END)
    
    if task in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        current_inp = inp.get()
        inp.delete(0, END)
        inp.insert(0, current_inp + task)
    elif task == '.':
        current_inp = inp.get()
        if not current_inp:
            inp.insert(0, '0.')
        elif current_inp[-1] in ['+', '-', '*', '/']:
            inp.delete(0, END)
            inp.insert(0, current_inp + '0.')
        else:
            inp.delete(0, END)
            inp.insert(0, current_inp + '.')
    elif task == '*':
        current_inp = inp.get()
        if not current_inp:
            inp.insert(0, '0')
        elif current_inp == '0' or current_inp[-1] == '*':
            pass
        elif current_inp[-1] in ['/', '+']:
            inp.delete(0, END)
            inp.insert(0, current_inp[:-1] + task)
        elif current_inp[-1] == '-':
            if (len(current_inp) >= 2) and (current_inp[-2] in ['/', '*']):
                inp.delete(0, END)
                inp.insert(0, current_inp[:-2] + task)
            else:
                inp.delete(0, END)
                inp.insert(0, current_inp[:-1] + task)
        else:
            inp.delete(0, END)
            inp.insert(0, current_inp + task)
    elif task == '/':
        current_inp = inp.get()
        if not current_inp:
            inp.insert(0, '0')
        elif current_inp == '0' or current_inp[-1] == '/':
            pass
        elif current_inp[-1] in ['*', '+']:
            inp.delete(0, END)
            inp.insert(0, current_inp[:-1] + task)
        elif current_inp[-1] == '-':
            if (len(current_inp) >= 2) and (current_inp[-2] in ['/', '*']):
                inp.delete(0, END)
                inp.insert(0, current_inp[:-2] + task)
            else:
                inp.delete(0, END)
                inp.insert(0, current_inp[:-1] + task)
        else:
            inp.delete(0, END)
            inp.insert(0, current_inp + task)
    elif task == '+':
        current_inp = inp.get()
        if not current_inp:
            inp.insert(0, '0')
        elif current_inp == '0' or current_inp[-1] == '+':
            pass
        elif current_inp[-1] in ['*', '/']:
            inp.delete(0, END)
            inp.insert(0, current_inp[:-1] + task)
        elif current_inp[-1] == '-':
            if (len(current_inp) >= 2) and (current_inp[-2] in ['/', '*']):
                inp.delete(0, END)
                inp.insert(0, current_inp[:-2] + task)
            else:
                inp.delete(0, END)
                inp.insert(0, current_inp[:-1] + task)
        else:
            inp.delete(0, END)
            inp.insert(0, current_inp + task)
    elif task == '-':
        current_inp = inp.get()
        if not current_inp or current_inp == '0':
            inp.insert(0, '-')
        elif current_inp[-1] == '-':
            pass
        elif current_inp[-1] == '+':
            inp.delete(0, END)
            inp.insert(0, current_inp[:-1] + task)
        else:
            inp.delete(0, END)
            inp.insert(0, current_inp + task)
    elif task == 'back':
        current_inp = inp.get()
        if current_inp:
            inp.delete(0, END)
            if current_inp[-1] == '.' and current_inp[-2] == '0' and len(current_inp) > 2:
                inp.insert(0, current_inp[:-2])
            else:
                inp.insert(0, current_inp[:-1])
        else:
            inp.insert(0, '0')
    elif task == '=':
        current_inp = inp.get()
        
        if not current_inp:
            inp.insert(0, temp)
        else:
            inp.delete(0, END)
            try:
                if current_inp[-1] in ['+', '-', '*', '/']:
                    current_inp = current_inp[:-1]
                
                result = eval(current_inp)
                
                if int(result) == result:
                    result = int(result)
                
                if result >= (10 ** 10):
                    inp.insert(0, "{:E}".format(result))
                else:
                    inp.insert(0, "{:,}".format(result))
            except:
                inp.insert(0, "ERROR!")
        flag = True
    elif task == "clear":
        inp.delete(0, END)
        inp.insert(END, '0')

flag = False

main = Tk()

main.title("Calculator")
main.resizable(0, 0)
main.iconbitmap(r".\data\icon.ico")

myFont = ("Bahnschrift", "14")

inp = Entry(main, width=20, bg="grey", fg="black", justify=RIGHT, font=("Helvetica", "16"), bd=7)
inp.insert(END, '0')
inp.grid(row=0, column=0, columnspan=4, ipady=15)

clear_button = Button(main, text='C', bg="lightgrey", fg="black", command=lambda: actions('clear'), font = myFont)
clear_button.grid(row=1, column=0, sticky=E+W)

divide_button = Button(main, text='/', bg="lightgrey", fg="black", command=lambda: actions('/'), font = myFont)
divide_button.grid(row=1, column=1, sticky=E+W)

mul_button = Button(main, text='*', bg="lightgrey", fg="black", command=lambda: actions('*'), font = myFont)
mul_button.grid(row=1, column=2, sticky=E+W)

back_button = Button(main, text='⌫', bg="lightgrey", fg="black", command=lambda: actions('back'), font = myFont)
back_button.grid(row=1, column=3, sticky=E+W)

seven_button = Button(main, text='7', bg="black", fg="white", command=lambda: actions('7'), font = myFont)
seven_button.grid(row=2, column=0, sticky=E+W)

eight_button = Button(main, text='8', bg="black", fg="white", command=lambda: actions('8'), font = myFont)
eight_button.grid(row=2, column=1, sticky=E+W)

nine_button = Button(main, text='9', bg="black", fg="white", command=lambda: actions('9'), font = myFont)
nine_button.grid(row=2, column=2, sticky=E+W)

minus_button = Button(main, text='-', bg="lightgrey", fg="black", command=lambda: actions('-'), font = myFont)
minus_button.grid(row=2, column=3, sticky=E+W)

four_button = Button(main, text='4', bg="black", fg="white", command=lambda: actions('4'), font = myFont)
four_button.grid(row=3, column=0, sticky=E+W)

five_button = Button(main, text='5', bg="black", fg="white", command=lambda: actions('5'), font = myFont)
five_button.grid(row=3, column=1, sticky=E+W)

six_button = Button(main, text='6', bg="black", fg="white", command=lambda: actions('6'), font = myFont)
six_button.grid(row=3, column=2, sticky=E+W)

plus_button = Button(main, text='+', bg="lightgrey", fg="black", command=lambda: actions('+'), font = myFont)
plus_button.grid(row=3, column=3, sticky=E+W)

one_button = Button(main, text='1', bg="black", fg="white", command=lambda: actions('1'), font = myFont)
one_button.grid(row=4, column=0, sticky=E+W)

two_button = Button(main, text='2', bg="black", fg="white", command=lambda: actions('2'), font = myFont)
two_button.grid(row=4, column=1, sticky=E+W)

three_button = Button(main, text='3', bg="black", fg="white", command=lambda: actions('3'), font = myFont)
three_button.grid(row=4, column=2, sticky=E+W)

equal_button = Button(main, text='=', bg="white", fg="black", command=lambda: actions('='), font = myFont)
equal_button.grid(row=4, column=3, rowspan=2, sticky=S+N+E+W)

zero_button = Button(main, text='0', bg="black", fg="white", command=lambda: actions('0'), font = myFont)
zero_button.grid(row=5, column=0, columnspan=2, sticky=E+W)

point_button = Button(main, text='.', bg="black", fg="white", command=lambda: actions('.'), font = myFont)
point_button.grid(row=5, column=2, sticky=E+W)

main.mainloop()