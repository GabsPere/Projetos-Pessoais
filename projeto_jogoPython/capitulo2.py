# Iremos usar uma biblioteca built in (Tkinter) para a interface gráfica

# Importando módulo
import tkinter as tk
from time import sleep
from backgroundcap2 import parte1, parte2, parte3

# --------------------
# 1- Criando a janela
window = tk.Tk()
# Passando a dimensão da janela
window.geometry("1000x800")
# Criando o título da janela
window.title("Cápitulo 2")

# --------------------
# 2- Criando o Frame - auxilia na disposição do conteúdo dentro da janela
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)
# --------------------
# 3- Adicionando o Label
label = tk.Label(frame, text=parte1)  # Posso usar essa parte no jogo.
label.pack(fill="x", expand=True)
# --------------------
# 4- Adicionando o input text

# Input da frase
frase_inp = tk.Entry(frame)  # Entrada de texto
frase_inp.pack(fill="x", expand=True)


# --------------------
# 5- Criando função para alterar o texto do label

def click():
    label.config(text=parte2)


# --------------------
# 6- Adicionando botão
bottao = tk.Button(frame, text="Continuar", command=click)
bottao.pack()

window.mainloop()
# --------------------
