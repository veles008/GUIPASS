from tkinter import *
import random
import os
import string

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join(desktop_path, "пароль.txt")

def generate_password2(length):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length):
        password += random.choice(characters)

    return password

def generate_password():
    dl = int(ttk.get())
    kol = int(ttk1.get())

    if dl and kol:
        file = open(file_path, 'w+')
        for i in range(kol):
            con = generate_password2(dl)
            file.write(con + '\n')
        file.close()


root = Tk()
root.title("Генератор паролей")
root.geometry("294x90+610+310")
root.resizable(width=False, height=False)


btn = Button(text="Сгенерировать пароль", command=generate_password, bg='green')
btn.grid(row=0, column=0, columnspan=4, sticky=EW)

btn1 = Label(text="Введите длину пароля:")
btn1.grid(row=1, column=0)
ttk = Entry()
ttk.grid(row=1, column=1)

btn2 = Label(text="Введите количество паролей:")
btn2.grid(row=2, column=0)
ttk1 = Entry()
ttk1.grid(row=2, column=1)


btn3 = Label(text="Файл с паролями на рабочем столе!", fg="green")
btn3.grid(row=3, column=0,columnspan=4, sticky=EW)

root.mainloop()
