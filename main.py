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

# botão C
b_c = Button(frame_body, text="C", width=22, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0)

# Números
b9 = Button(frame_body, text="9", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x=240, y=100)
b8 = Button(frame_body, text="8", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x=120, y=100)
b7 = Button(frame_body, text="7", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x=0, y=100)
b4 = Button(frame_body, text="4", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=200)
b5 = Button(frame_body, text="5", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x=120, y=200)
b6 = Button(frame_body, text="6", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x=240, y=200)
b1 = Button(frame_body, text="1", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=300)
b2 = Button(frame_body, text="2", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x=120, y=300)
b1 = Button(frame_body, text="1", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x=240, y=300)
b0 = Button(frame_body, text="0", width=22, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b0.place(x=0, y=400)
b_ponto = Button(frame_body, text=".", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=240, y=400)

# Lateral
b_resto = Button(frame_body, text="%", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_resto.place(x=240, y=0)
b_div= Button(frame_body, text="/", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=360, y=0)
b_multi = Button(frame_body, text="*", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_multi.place(x=360, y=100)
b_menos = Button(frame_body, text="-", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=360, y=200)
b_mais = Button(frame_body, text="+", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=360, y=300)
b_igual = Button(frame_body, text="=", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=360, y=400)

janela.mainloop()