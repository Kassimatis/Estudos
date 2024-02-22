import random
from tkinter import *

def adivinhar_gay(lista_gays):
    random.shuffle(lista_gays)
    gay_mais = random.choice(lista_gays)
    return gay_mais

gays = ["Basck", "Jairo", "Alexandre", "Patriota", "Rodo"]
gay_mais = adivinhar_gay(gays)

def mostrar_resultado():
    resultado_label.config(text="Após uma intensa análise científica e algoritmos de última geração,")
    janela.after(2000, lambda: resultado_label.config(text="descobri que..."))
    janela.after(4000, lambda: resultado_label.config(text=f"O mais gay do grupo é... {gay_mais}!"))

janela = Tk()
janela.title("Rataria Revelações")
janela.geometry("400x400")

resultado_label = Label(janela, text="Pressione o botão para descobrir o segredo revelador")
resultado_label.pack(pady=20)

botao = Button(janela, text="Descobrir", command=mostrar_resultado)
botao.pack()

janela.mainloop()
