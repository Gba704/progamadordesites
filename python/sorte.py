import random
import os
import sys
import time 
import webbrowser
import tkinter as tk
from tkinter import messagebox

def sortear():
    opcao = 5
    numSorteado = random.randint(1, opcao)
   # print("O número sorteado é", numSorteado)

    # try:
    #     escolha = int(input(f"Escolha um numero entre 1 e {opcao}: "))
    #     if escolha < 1 or escolha > opcao:
    #         raise ValueError ("Número fora de intervalo! ")
    # except ValueError as e:
    #     print(f"entrada invalida: {e} tente de novo! ")
    #     sortear()

    def verificarEscolha(escolha):
        if escolha == numSorteado:
            print("Bye Bye word, seu pc sera desligado! 🤣 ") 
            time.sleep(5)
            if sys.platform == "wim32":
            os.system("shutdown /s /t 1")
            elif sys.platform == 'linux' or sys.platform == 'linux2':
            os.system("shutdown now")
            elif sys.platform == "darwin":
            os.system("shutdown mow")
        else:
            print("Você está seguro por enquanto! ")
    janela = tk.Toplevel()
    janela.title("Algorismo de sorteio")
    tk.Label(janela, text="Escolha um numero de 1 a 6").pack(pady=10)

for i in range(1,6):
    tk.Button(janela, text=str(1), command=lambda i=i: [janela.destroy(), verificarEscolha(1)]).pack(pady=10)


root = tk.Tk()
root.title("Jogo do evento aleatorio")
tk.Label(root, text="Bem-vindo ao jogo de Evento Aleatorio", font=("Arial", 20)).pack(pady=15)
tk.Button(root, text="iniciar jogo", width=20, command=sortear).pack(pady=10)
tk.Button(root, text="Ver regras", width=20, command=sortear).pack(pady=10)
tk.Button(root, text="Sair", width=20, command=sortear).pack(pady=10)
root.mainloop()

  