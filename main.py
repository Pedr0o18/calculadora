# 1 Passo: Importando a Biblioteca

from tkinter import *
from tkinter import ttk

# Cores

cor1 = "#1e1f1e" # preta
cor2 = "#feffff" # branca
cor3 = "#38576b" # azul
cor4 = "#ECEFF1" # cinza
cor5 = "#FFAB40" # laranja

# 2 Passo: Criando e Configurando a Janela

janela = Tk()
janela.title("Calculadora")
janela.geometry("470x636")
janela.config(bg=cor1)

# 3 Passo: Separando e Configurando os Frames

frame_display = Frame(janela, width=470, height=100, bg=cor3)
frame_display.grid(row=0, column=0)

frame_body = Frame(janela, width=470, height=536)
frame_body.grid(row=1, column=0)

# 4 Passo: Criando Botões

b1 = Button(frame_body, text="C", width=22, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_body, text="%", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=240, y=0)
b3 = Button(frame_body, text="/", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x=360, y=0)

janela.mainloop()