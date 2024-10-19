from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk()
        self.botao = Button(self.janela_principal, text='Clique aqui', command=self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair' , command=self.quit)
        self.botao.pack()
        self.botao_sair.pack()
        self.janela_principal.mainloop()

    def quit(self):
        self.janela_principal.destroy()

    def hello_world(self):
        messagebox.showinfo('Aula de RAD!', 'Olá, mundo!')

gui = MinhaGUI ()

import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc= peso / (altura ** 2)
        if imc < 18.5:
            situacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            situacao = "Peso normal"
        elif 25 <= imc < 29.9:
            situacao = "Sobrepeso"
        else:
            situacao = "Obesidade"
        messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f} \nSituação: {situacao}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

janela = tk.Tk()
janela.title("Calculadora de IMC")

label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=10, pady=10)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

label_altura = tk.Label(janela, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=10, pady=10)
entry_altura = tk.Entry(janela)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.grid(row=2, column=0, columnspan=2, pady=20)

janela.mainloop()
                  