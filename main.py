import tkinter as tk
from tkinter import *
import os
from time import strftime

#   definindo título, tamanho minimo da janela e cor de background
root = tk.Tk()
root.title('Clock')
root.geometry("600x320")
root.minsize(300, 240)
root.configure(background = '#1d1d1d')

#   função para pegar nome de usuario do login do sistema operacional
def get_welcome():
    user_name = os.getlogin()
    welcome.config(text = 'Welcome, ' + user_name)

#   função que define a data: dia da semana, data, mês, dia
def get_date():
    current_date = strftime('%a, %b %y')
    date.config(text = current_date)

#   fução que define as horas HH:MM:SS
def get_hours():
    current_hour = strftime('%H:%M:%S')
    hours.config(text=current_hour)
    hours.after(1000, get_hours)

#   definindo margem acima
margem = tk.Canvas(root, width=600, height=60, bg='#1d1d1d', bd=0, highlightthickness=0, relief='ridge')
#   gerenciador para exibir o widget
margem.pack()

#   Label para definir cor do fundo, cor da fonte, fonte a ser usada e tamanho da fonte
welcome = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Bebas Neue', 20))
welcome.pack()

date = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Bebas Neue', 18))
date.pack(pady=2)

hours = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('Bebas Neue', 64))
hours.pack(pady=2)

#   Chamada de funções
get_welcome()
get_date()
get_hours()

#   loop para manter programa aberto
root.mainloop()
