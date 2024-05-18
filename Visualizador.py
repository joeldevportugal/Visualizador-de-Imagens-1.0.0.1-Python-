# Importar as bibliotecas a usar ----------------------------------------------------------
from tkinter import messagebox
import customtkinter
import tkinter as tk
from tkinter import Label, Listbox, Menu, filedialog, Scrollbar
import os
from PIL import Image, ImageTk
import time
#-----------------------------------------------------------------------------------------
# criar as Funções e variaveis  ----------------------------------------------------------
# Função para iniciar a apresentação automática
def iniciar_auto():
    global auto_running
    auto_running = True
    apresentar_proxima_imagem_auto()

# Função para parar a apresentação automática
def parar_auto():
    global auto_running
    auto_running = False
    messagebox.showinfo("A sua Apresentação", "Sua Apresentação esta parada")

def apresentar_proxima_imagem_auto():
    global auto_running
    if auto_running:
        proxima_imagem()
        if indice_imagem_atual == len(imagens) - 1:
            # Esta é a última imagem, então exibe a mensagem de fim da apresentação
            messagebox.showinfo("Fim da Apresentação", "Sua Apresentação Chegou ao Fim")
            auto_running = False  # Parar a apresentação automática após exibir a mensagem de fim
        else:
            Janela.after(1000, apresentar_proxima_imagem_auto)

# Variável para armazenar o índice da imagem atual
indice_imagem_atual = 0
# Função para abrir a pasta e carregar imagens ---------------------------------------
def abrir_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        carregar_imagens(pasta)

def carregar_imagens(pasta):
    global imagens, indice_imagem_atual
    # Limpar a lista de ficheiros
    LFicheiros.delete(0, tk.END)
    # Listar todos os arquivos na pasta
    arquivos = os.listdir(pasta)
    imagens = [arq for arq in arquivos if arq.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    
    for img in imagens:
        LFicheiros.insert(tk.END, os.path.join(pasta, img))

    if imagens:
        indice_imagem_atual = 0
        mostrar_imagem(os.path.join(pasta, imagens[indice_imagem_atual]))

def mostrar_imagem(caminho_imagem):
    # Carregar a imagem e exibi-la no label
    img = Image.open(caminho_imagem)
    img = img.resize((450, 350), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    
    Limagem.config(image=img_tk)
    Limagem.image = img_tk
    # Atualizar o label de número de imagens
    total_imagens = len(imagens)
    LNumero.config(text=f'Imagem {indice_imagem_atual + 1} de {total_imagens}')

def atualizar_selecao(evt):
    global indice_imagem_atual
    indices = LFicheiros.curselection()
    if indices:
        indice_imagem_atual = indices[0]
        caminho_imagem = LFicheiros.get(indice_imagem_atual)
        mostrar_imagem(caminho_imagem)
        LFicheiros.see(indice_imagem_atual)    

def proxima_imagem():
    global indice_imagem_atual
    if imagens:
        if indice_imagem_atual < len(imagens) - 1:
            indice_imagem_atual += 1
            LFicheiros.selection_clear(0, tk.END)
            LFicheiros.selection_set(indice_imagem_atual)
            LFicheiros.activate(indice_imagem_atual)
            mostrar_imagem(LFicheiros.get(indice_imagem_atual))
            LFicheiros.see(indice_imagem_atual)  # Garante que o item selecionado seja visível na Listbox
        elif indice_imagem_atual == len(imagens) - 1:
            # Esta é a última imagem, então exiba a mensagem de fim da apresentação
            messagebox.showinfo("Fim da Apresentação", "Sua Apresentação Chegou ao Fim")

def Limpar():
     # Limpar a imagem
    Limagem.config(image='')
    Limagem.image = None
    # Limpar a lista de arquivos
    LFicheiros.delete(0, tk.END)
    # Atualizar o label de número de imagens
    LNumero.config(text='Imagem 0 de 0')
    messagebox.showinfo("Limpeza", "Seus Dados Foram Limpos Com Sucesso")

def imagem_anterior():
    global indice_imagem_atual
    if imagens and indice_imagem_atual > 0:
        indice_imagem_atual -= 1
        LFicheiros.selection_clear(0, tk.END)
        LFicheiros.selection_set(indice_imagem_atual)
        LFicheiros.activate(indice_imagem_atual)
        mostrar_imagem(LFicheiros.get(indice_imagem_atual))
        LFicheiros.see(indice_imagem_atual)  # Garante que o item selecionado seja visível na Listbox
    elif indice_imagem_atual == 0:
        messagebox.showinfo("Início da Apresentação", "Você está na primeira imagem da lista.")

def sair():
    resposta = messagebox.askyesno("Fechar Aplicação", "Você deseja fechar a aplicação?")
    if resposta:
        Janela.quit()

def Sobre ():        
     messagebox.showinfo("Versão", "Versão 1.0.0.1 By DevJoel Portugal ")

def Autor ():        
     messagebox.showinfo("Autor", "Autor: Joel António Gonçalves Tigeleiro\n"+"Idade 32\n"+"Pais: Portugal")
#----------------------------------------------------------------------------------------------------
# Definir as cores a usar ------------------------------------------------------------
co1 = "#FFFFFF"  # cor branca para a janela
co2 = "#F9F8F4"  # cor Cinza Claro Para Botões 
co3 = "#000000"  # cor Preta para a Letra
# ------------------------------------------------------------------------------------
# Configurar a janela principal ------------------------------------------------------
Janela = customtkinter.CTk()
Janela.geometry('480x493+100+100')
Janela.resizable(False, False)
Janela.config(bg=co1)
Janela.title('Visualizador dev Joel 1.0.0.1 Portugal Dev Joel Portugal')
# ------------------------------------------------------------------------------------
# Criar a barra de menu ------------------------------------------------------------
menu_bar = Menu(Janela)
# ----------------------------------------------------------------------------------
# Criar o primeiro submenu ---------------------------------------------------------
submenu1 = Menu(menu_bar, tearoff=0)
submenu1.add_command(label="Abrir", font=('arial 12'), command=abrir_pasta)
submenu1.add_command(label="Limpar", font=('arial 12'), command=Limpar)
submenu1.add_command(label="Sair", font=('arial 12'), command=sair)
# ---------------------------------------------------------------------------------
# Criar o segundo submenu ----------------------------------------------------------
submenu2 = Menu(menu_bar, tearoff=0)
submenu2.add_command(label="Sobre", font=('arial 12'), command=Sobre)
submenu2.add_command(label="Autor", font=('arial 12'), command=Autor)
# ---------------------------------------------------------------------------------
# Adicionar os submenus à barra de menu -------------------------------------------
menu_bar.add_cascade(label="Menu", menu=submenu1)
menu_bar.add_cascade(label="Ajuda", menu=submenu2)
# ---------------------------------------------------------------------------------
# Configurar a barra de menu na janela principal ----------------------------------
Janela.config(menu=menu_bar)
# ---------------------------------------------------------------------------------
# Criar o label para apresentar a imagem ------------------------------------------
Limagem = Label(Janela)
Limagem.place(x=5, y=5)
# ---------------------------------------------------------------------------------
# Criar a Listbox e Scrollbar -----------------------------------------------------
LFicheiros = Listbox(Janela, width=53, height=7, font=('Arial 14'))
LFicheiros.place(x=5, y=390, width=560, height=150)
LFicheiros.bind('<<ListboxSelect>>', atualizar_selecao)
scrollbar = Scrollbar(Janela, command=LFicheiros.yview)
scrollbar.place(x=565, y=390, height=150)
LFicheiros.config(yscrollcommand=scrollbar.set)
#-----------------------------------------------------------------------------------
# Criar Botões --------------------------------------------------------------------
BtnAnterior = customtkinter.CTkButton(Janela, text='Anterior', width=29, bg_color=co1, command=imagem_anterior, fg_color=co2, text_color=co3)
BtnAnterior.place(x=5, y=450)
BtnProximo = customtkinter.CTkButton(Janela, text='Proximo', width=29, bg_color=co1, command=proxima_imagem, fg_color=co2, text_color=co3)
BtnProximo.place(x=70, y=450)
BtnAuto = customtkinter.CTkButton(Janela, text='iniciar Auto', width=29, bg_color=co1, command=iniciar_auto, fg_color=co2, text_color=co3)
BtnAuto.place(x=140, y=450)
BtnParar = customtkinter.CTkButton(Janela, text='Parar Auto', width=29, bg_color=co1, command=parar_auto, fg_color=co2, text_color=co3)
BtnParar.place(x=230, y=450)
# ---------------------------------------------------------------------------------
# Criar o label para exibir o número de imagens -----------------------------------
LNumero = Label(Janela, text='Imagem 0 de 0', font=('arial 15'), bg=co1)
LNumero.place(x=410, y=565)
# ---------------------------------------------------------------------------------
Janela.mainloop()
