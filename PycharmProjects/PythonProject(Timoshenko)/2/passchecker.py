import math
import sqlite3
import tkinter as tk
from random import choice
from tkinter import messagebox

conn = sqlite3.connect("../test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS passwords(id integer primary key, password varchar(255))")

def generator():
    digits = '0123456789'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '!@#$%^&*()-_=+[]{};:.<>/?|~`'
    chars = digits+uppercase+lowercase+punctuation
    password1 = ''
    for i in range(12):
        password1 += choice(chars)
    if quick_check(password1):
        entry.insert(0, password1)
        print(password1)

def quick_check(password1):
    passlen = len(password1)
    E = passlen * math.log2(94)
    if E < 78:
        return False
    else:
        return True

def calculate():
    password = entry.get()
    passlen = len(password)
    E = passlen * math.log2(94)
    if E < 78:
        messagebox.showwarning("Внимание!", "Уровень защиты вашего пароля: Низкий")
    elif E <= 105:
        messagebox.showwarning("Внимание!", "Уровень защиты вашего пароля: Средний")
    elif E <= 131:
        messagebox.showwarning("Внимание!", "Уровень защиты вашего пароля: Высокий")
    elif E > 131:
        messagebox.showwarning("Внимание!", "Уровень защиты вашего пароля: Максимальный")

def save():
    password1 = entry.get()
    if quick_check(password1):
        cursor.execute("INSERT INTO passwords VALUES(%s)", (password1, ))
    else:
        messagebox.showerror("Ошибка!","Ваш пароль слишком слабый")


root = tk.Tk()
root.geometry("400x350")
root.title("Мастер паролей")
lbl1 = tk.Label(root, text="Placeholder", font=16)
entry = tk.Entry(root, width=25)
frame1 = tk.Frame(root)
btn1 = tk.Button(frame1, text="Проверить пароль", command=calculate)
btn2 = tk.Button(frame1, text="Сгенерировать пароль", command=generator)
btn3 = tk.Button(frame1, text="Сохранить пароль", command=save)
btn4 = tk.Button(root, text="Параметры пароля")
lbl1.pack(side="top", padx=5, pady=5)
entry.pack(side="top", padx=5, pady=5)
frame1.pack(side="top", padx=5, pady=5)
btn1.pack(side="left", padx=5,pady=5)
btn2.pack(side="left", padx=5,pady=5)
btn3.pack(side="left", padx=5,pady=5)
root.mainloop()