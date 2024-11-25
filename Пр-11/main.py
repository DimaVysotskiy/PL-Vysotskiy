from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinter.ttk import Combobox




#for task 1
def calculate():
    first_digit = e.get()
    second_digit = e1.get()
    sign = c.get()
    type_digit = sel1.get()
    try:
        if type_digit == 1:
            if sign == '+':
                answer = int(first_digit) + int(second_digit)
            elif sign == '-':
                answer = int(first_digit) - int(second_digit)
            elif sign == '*':
                answer = int(first_digit) * int(second_digit)
            elif sign == '/':
                answer = int(first_digit) / int(second_digit)
            l_answer.configure(text=answer)
        elif type_digit == 2:
            if sign == '+':
                answer = float(first_digit) + float(second_digit)
            elif sign == '-':
                answer = float(first_digit) - float(second_digit)
            elif sign == '*':
                answer = float(first_digit) * float(second_digit)
            elif sign == '/':
                answer = float(first_digit) / float(second_digit)
            l_answer.configure(text=answer)
    except Exception as ex:
        l_answer.configure(text='Error!!!')
        print(ex)




#for task 2
def click():
    a = sel.get()
    if a == 1:
        messagebox.showinfo('Your choice', f'Checkbox №{a}', parent=window)
    elif a == 2:
        messagebox.showinfo('Your choice', f'Checkbox №{a}', parent=window)
    elif a == 3:
        messagebox.showinfo('Your choice', f'Checkbox №{a}', parent=window)




#for task 3
def open_file():
    f = filedialog.askopenfilename(defaultextension='txt')
    with open(f, '+r') as file:
        a = file.read()
        text.insert(1.0, a)




def save():
    f = filedialog.askopenfilename(defaultextension='txt')
    with open(f, '+r') as file:
        a = text.get(1.0, END)
        file.write(a)
        text.delete(1.0, END)




#mainwin
window = Tk()
window.title('VysotskiyD.V.')
window.geometry('600x300')
window.resizable(height=False, width=False)




#for frame
tab_control = ttk.Notebook(window)
task1 = ttk.Frame(tab_control)
task2 = ttk.Frame(tab_control)
task3 = ttk.Frame(tab_control)
tab_control.add(task1, text='Task1')
tab_control.add(task2, text='Task2')
tab_control.add(task3, text='Task3')
tab_control.pack(fill='both', expand=True)




#wintask1
preview_t1 = Label(task1, text='Task №1 "Calculator"')
preview_t1.grid(row=2, column=1)

c = Combobox(task1, width=1)
c['values'] = ('+', '-', '*', '/')
c.grid(row=3, column=1, rowspan=2)

e = Entry(task1, width=15)
e.grid(row=3, column=2)

e1 = Entry(task1, width=15)
e1.grid(row=4, column=2)

l = Label(task1, text='-' * 18)
l.grid(row=5, column=2)

l_answer = Label(task1, text='?' * 16)
l_answer.grid(row=6, column=2)

b = Button(task1, text='To calculate', command=calculate)
b.grid(row=6, column=1)

l_settings = Label(task1, text='Settings')
l_settings.place(x=270, y=0)

l_settings = Label(task1, text='Type of numbers:')
l_settings.place(x=270, y=20)

sel1= IntVar()
sel1.set(1)

rad1 = Radiobutton(task1, text='Int', value=1, variable=sel1)
rad1.place(x=370, y=20)

rad2 = Radiobutton(task1, text='Float', value=2, variable=sel1)
rad2.place(x=420, y=20)




#wintask2
preview_t2 = Label(task2, text='Task №2 "Checkbox"')
preview_t2.grid(row=2, column=1)

sel = IntVar()

rad1 = Radiobutton(task2, text='Var1', value=1, variable=sel)
rad1.grid(row=3, column=1, sticky='nw')

rad2 = Radiobutton(task2, text='Var2', value=2, variable=sel)
rad2.grid(row=4, column=1, sticky='nw')

rad3 = Radiobutton(task2, text='Var3', value=3, variable=sel)
rad3.grid(row=5, column=1, sticky='nw')

choice_b = Button(task2, text='Choice?', command=click)
choice_b.grid(row=6, column=1, sticky='nw')




#wintask3
preview_t3 = Label(task3, text='Task №3 "Working with text"')
preview_t3.pack(anchor='nw')

text = scrolledtext.ScrolledText(task3, width=50, height=20, bg='white', fg='black')
text.pack(anchor='nw')

open_b = Button(task3, text='Open file', command=open_file)
open_b.place(x=424, y=20)

save_b = Button(task3, text='Save as', command=save)
save_b.place(x=424, y=46, width=59)




window.mainloop()