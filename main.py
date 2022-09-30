from tkinter import *
from tkinter import Tk, StringVar, ttk

from PIL import Image, ImageTk

co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # verde
co9 = "#e9edf5"  # background

# Criando janela
janela = Tk()
janela.title('JAO')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")


# Criando frames (div)
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300,
                   bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


# Manipulando imagem
app_img = Image.open('./img/book.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img,
                 text=' Inventário Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

janela.mainloop()
