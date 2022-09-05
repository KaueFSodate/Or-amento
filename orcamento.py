from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Criando janela
janela = Tk()   ## Criando janela
janela.title = ("") ## Titulo janela
janela.geometry('250x400') ## Tamanho janela
janela.configure(background="white") ## Cor de fundo da janela
janela.resizable(width=FALSE, height=FALSE) ## Tamanho máximo janela

style = ttk.Style(janela)
style.theme_use("clam")

# Frames


# Frame cima

framecima = Frame(janela, width=300, height=50, bg="#87CEFA", relief="flat") ## Atribultos
framecima.grid(row=0, column=0) ## Localização do frame

# Logo

app_ = Label(framecima, text="Orçamento", compound=LEFT, padx=5, relief="flat", anchor=NW, font=("Verdana 20"), bg="#87CEFA") ## Atribultos
app_.place(x=0, y=0) ## Localização do logo

# Abrindo imagem

app_img = Image.open("logo2323.png") ## Abrir imagem
app_img = app_img.resize((40, 40)) ## Tamanho da imagem
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(framecima, image=app_img, compound=LEFT, padx=5, relief="flat", anchor=NW, font=("Verdana 20"), bg="#87CEFA") ## Atribultos Imagem
app_logo.place(x=160, y=0) ## Localização imagem

# Frame linha

app_linha = Label(framecima, width=295, relief="flat", anchor=NW, font=("Ivy 1"), bg="black", fg="white") ## Atribultos para fazer a linha
app_linha.place(x=0, y=47) ## Localização do frame


# Frame meio

framemeio = Frame(janela, width=300, height=90, bg="#87CEFA", relief="flat") ## Atribultos do Frame meio
framemeio.grid(row=1, column=0) ## Localização do frame

# Função do botão


def calcular():
    renda_mensal = float(e_valor.get())  ## Variável que será colocada o valor digitado pelo usuário

    obter_50_percento = (50 / 100) * renda_mensal ## Variável que ira fazer o calculo de 50%
    obter_30_percento = (30 / 100) * renda_mensal ## Variável que ira fazer o calculo de 30%
    obter_20_percento = (20 / 100) * renda_mensal ## Variável que ira fazer o calculo de 20%

    l_necessidades["text"] = ("R${:,.2f}".format(obter_50_percento))
    l_quer["text"] = ("R${:,.2f}".format(obter_30_percento))        ## Ira aparecer os valores
    l_poupança["text"] = ("R${:,.2f}".format(obter_20_percento))


# TEXTO meio

app_ = Label(framemeio, text="Entra a sua renda mensal",relief="flat", anchor=NW, font=("Ivy 10"), bg="#87CEFA", fg="black") ## Atribultos texto
app_.place(x=7, y=15) ## Localização

# Inserir o valor

e_valor = Entry(framemeio, width=10, font=("Ivy 14"), justify="center", relief="solid") ## Inserir o valor pelo usuário em uma caixa de texto
e_valor.place(x=10, y=40) ## Localização


# BOTÃO

b_calcular = Button(framemeio, command=calcular, text="Calcular".upper(
), relief=RIDGE, anchor=NW, font=("Ivy 8"), bg="white", fg="black") ## Atributos botão
b_calcular.place(x=150, y=40) ## Localização


# Frame baixo

framebaixo = Frame(janela, width=300, height=290, bg="#4682B4", relief="flat") ## Atributos
framebaixo.grid(row=2, column=0)## Localização

app_ = Label(framebaixo, text="Seus valores de 50% 30% 20%", width= 250,
             relief="flat", anchor=NW, font=("Verdana 11"), bg="#6495ED", fg="black") ## Atributos texto
app_.place(x=0, y=0) ## Localização

l_tnecessidades = Label(framebaixo, text="Necessidades:", relief="flat", width=35, anchor=NW, font=("Verdana 10"), bg="#4682B4", fg="black") ## Atributos texto
l_tnecessidades.place(x=10, y=40) ## Localização

l_necessidades = Label(framebaixo, relief="flat", width=22, anchor=NW, font=("Verdana 10"), bg="white", fg="black") ## Atributos texto
l_necessidades.place(x=10, y=75) ## Localização

l_tquer = Label(framebaixo, text="Gastos:", relief="flat", width=35, anchor=NW, font=("Verdana 10"), bg="#4682B4", fg="black") ## Atributos texto
l_tquer.place(x=10, y=115) ## Localização

l_quer = Label(framebaixo, relief="flat", width=22, anchor=NW, font=("Verdana 10"), bg="white", fg="black") ## Atributos texto
l_quer.place(x=10, y=145) ## Localização

l_tpoupança = Label(framebaixo, text="Poupança:", relief="flat", width=35, anchor=NW, font=("Verdana 10"), bg="#4682B4", fg="black") ## Atributos texto
l_tpoupança.place(x=10, y=185) ## Localização

l_poupança = Label(framebaixo, relief="flat", width=22, anchor=NW, font=("Verdana 10"), bg="white", fg="black") ## Atributos texto
l_poupança.place(x=10, y=215) ## Localização


janela.mainloop()
