from tkinter import *

ROOT = Tk()
ROOT.title('Calculator') 

def button_click(char, e):
    if 'Error' in e.get(): 
        e.delete(0,END)
        current = e.get()
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(char)) 

def clear(e):
    e.delete(0, END) 

def button_equal(e):
    try:
        num = eval(e.get())
    except Exception:
        e.delete(0, END)
        e.insert(0,'Error') 
    else:
        e.delete(0, END)
        e.insert(0,num) 

def main(root):
    e = Entry(root, width = 35, borderwidth = 10)
    e.grid(row = 0, column = 0, columnspan = 30, padx = 10, pady = 10) 

    button = {}
    button['button0'] = Button(root, text = '0',padx = 40, pady = 20, command = lambda: button_click(0, e), bd = 5) 
    button['button1'] = Button(root, text = '1',padx = 40, pady = 20, command = lambda: button_click(1, e), bd = 5) 
    button['button2'] = Button(root, text = '2',padx = 40, pady = 20, command = lambda: button_click(2, e), bd = 5) 
    button['button3'] = Button(root, text = '3',padx = 40, pady = 20, command = lambda: button_click(3, e), bd = 5) 
    button['button4'] = Button(root, text = '4',padx = 40, pady = 20, command = lambda: button_click(4, e), bd = 5) 
    button['button5'] = Button(root, text = '5',padx = 40, pady = 20, command = lambda: button_click(5, e), bd = 5) 
    button['button6'] = Button(root, text = '6',padx = 40, pady = 20, command = lambda: button_click(6, e), bd = 5) 
    button['button7'] = Button(root, text = '7',padx = 40, pady = 20, command = lambda: button_click(7, e), bd = 5) 
    button['button8'] = Button(root, text = '8',padx = 40, pady = 20, command = lambda: button_click(8, e), bd = 5) 
    button['button9'] = Button(root, text = '9',padx = 40, pady = 20, command = lambda: button_click(9, e), bd = 5) 

    for i in range(1,10):
        subtrahend = 1
        button_row = 3 
        if i >= 4 and i <= 7:  
            subtrahend = 4
            button_row = 2 
        if i >= 7 and i <= 9:  
            subtrahend = 7
            button_row = 1
        button[f'button{i}'].grid(row = button_row, column = i - subtrahend) 
    button['button0'].grid(row = 4, column = 1)

    button_clear = Button(root, text = 'CE', padx = 40, pady = 20, command = lambda: clear(e), bd = 5)
    button_equals = Button(root, text = '=', padx = 40, pady = 20, command = lambda: button_equal(e), bd = 5)
    button_multiply = Button(root, text = '*', padx = 40, pady = 20, command = lambda: button_click('*', e), bd = 5)
    button_divide = Button(root, text = '/', padx = 40, pady = 20, command = lambda: button_click('/', e), bd = 5)
    button_add = Button(root, text = '+', padx = 38, pady = 20, command = lambda: button_click('+', e), bd = 5)
    button_subtract = Button(root, text = '-', padx = 41, pady = 20, command = lambda: button_click('-', e), bd = 5)
    button_dot = Button(root, text = '.', padx = 41, pady = 20, command = lambda: button_click('.',e), bd = 5)

    button_multiply.grid(row = 4, column = 0)
    button_divide.grid(row = 4, column = 2)
    button_add.grid(row = 5, column = 0)
    button_subtract.grid(row = 5, column = 2)
    button_equals.grid(row = 5, column = 1)
    button_clear.grid(row = 6, column = 1) 
    button_dot.grid(row = 6, column = 0)

def run(root):
    main(root)
    root.mainloop()

run(ROOT) 
