from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image, ImageTk

from tkcalendar import Calendar, DateEntry
from datetime import date

from view import *

co0 = "#2e2d2b"  # preto
co1 = "#feffff"  # branco
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # azul
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

# Criando funções ---------------------
global tree


# Função inserir
def inserir():
    global imagem, imagem_string, l_imagem

    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    model = e_model.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso!', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_model.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    mostrar()


# Função Atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        e_nome.delete(0, 'end')
        e_local.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_model.delete(0, 'end')
        e_cal.delete(0, 'end')
        e_valor.delete(0, 'end')
        e_serial.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_local.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_model.insert(0, treev_lista[4])
        e_cal.insert(0, treev_lista[5])
        e_valor.insert(0, treev_lista[6])
        e_serial.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem

            nome = e_nome.get()
            local = e_local.get()
            descricao = e_descricao.get()
            model = e_model.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serial.get()
            imagem = imagem_string

            if imagem == "":
                imagem = e_serial.insert(0, treev_lista[7])

            lista_atualizar = [nome, local, descricao,
                               model, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos')
                    return

            atualizar_form(lista_atualizar)
            messagebox.showinfo(
                'Sucesso!', 'Os dados foram inseridos com sucesso')

            e_nome.delete(0, 'end')
            e_local.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_model.delete(0, 'end')
            e_cal.delete(0, 'end')
            e_valor.delete(0, 'end')
            e_serial.delete(0, 'end')

            b_confirmar.destroy()
            mostrar()

        b_confirmar = Button(frameMeio, command=update, width=13, text="Confirmar".upper(), overrelief=RIDGE,
                             font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# Função Deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]

        deletar_form([valor])

        messagebox.showinfo(
            'Sucesso!', 'Os dados foram deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


# Função para escolher imagem
global imagem, imagem_string, l_imagem


def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


# Função para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_item(valor)

    imagem = iten[0][8]
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


# Trabalhando no framaCima ----------------------------------
# Manipulando imagem
app_img = Image.open('./img/book.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img,
                 text=' Lista de Compras', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no framaMeio -------------------------------------

# Criando entradas
l_nome = Label(frameMeio, text="Nome", height=1, anchor=NW,
               font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

l_local = Label(frameMeio, text="Sala/Área", height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

l_descricao = Label(frameMeio, text="Descricao", height=1, anchor=NW,
                    font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_model = Label(frameMeio, text="Marca/Model", height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_model.place(x=10, y=100)
e_model = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_model.place(x=130, y=101)

l_cal = Label(frameMeio, text="Data da compra", height=1, anchor=NW,
              font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, Background='darkblue',
                  borderwidth=2, year=2022)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text="Valor da compra", height=1, anchor=NW,
                font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

l_serial = Label(frameMeio, text="Número de série", height=1, anchor=NW,
                 font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)


# Criando botões -------------------

# Botão carregar
l_carregar = Label(frameMeio, text="Imagem do item", height=1, anchor=NW,
                   font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
b_carregar = Button(frameMeio, command=escolher_imagem, width=29, text="Carregar".upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE,
                    font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)


# Botão inserir
img_add = Image.open('./img/add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

b_inserir = Button(frameMeio, command=inserir, image=img_add, width=95, text="  Adicionar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,
                   font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)


# Botão atualizar
img_update = Image.open('./img/att.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

b_update = Button(frameMeio, command=atualizar, image=img_update, width=95, text="  Atualizar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,
                  font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

# Botão deletar
img_delete = Image.open('./img/delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)

b_delete = Button(frameMeio, command=deletar, image=img_delete, width=95, text="  Apagar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,
                  font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

# Botão ver imagem
img_item = Image.open('./img/look.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)

b_item = Button(frameMeio, command=ver_imagem, image=img_item, width=95, text="  Ver item".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,
                font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)

# Labels Quantidade todal e Valores
l_total = Label(frameMeio, text="", width=14, height=2, pady=5, anchor=CENTER,
                font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)

l_total_ = Label(frameMeio, text="   Valor total de todos os itens  ", height=1, anchor=CENTER,
                 font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)


l_qtd = Label(frameMeio, text="", width=14, height=2, pady=5, anchor=CENTER,
              font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=90)

l_qtd_ = Label(frameMeio, text="  Quantidade total de itens  ", height=1, anchor=CENTER,
               font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=450, y=92)


# Tabela -----------------------------

def mostrar():
    global tree

    tabela_head = ['#Item', 'Nome',  'Sala/Área', 'Descrição',
                   'Marca/Modelo', 'Data da compra', 'Valor da compra', 'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",
                        columns=tabela_head, show="headings")

    # scroll verdical
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # scroll horizontal
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center",
          "center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # ajuste da largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = [0000, 00]

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = (len(quantidade)-2)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()
janela.mainloop()
