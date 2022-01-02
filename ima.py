from tkinter import *

def funct(numimg):
    image = PhotoImage(file="image"+str(numimg)+".png")
    label = Label(image=image)
    label.grid(row = row_no+1, column = 0, columnspan = num_of_cols)

def make_funct(number):
    return (lambda: funct(number))

root= Tk()
row_no = -1
buttons = []
num_of_cols = 3
root.resizable(0, 0)
numfiles = 6

for x in range(0, numfiles):
    if(x % num_of_cols is 0):
        row_no+=1

    buttons.append(Button(root, text = "Button "+str(x), bg = '#4098D3', width = 30,height = 13,command = make_funct(x)))
    buttons[x].grid(row = row_no, column = x % num_of_cols)

root.mainloop()