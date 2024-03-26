import tkinter as tk
import numpy as np
import math
from scipy.stats import norm

def call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    delta = norm.cdf(d1)

    c_t = S * delta - K * np.exp(-r * T) * norm.cdf(d1 - sigma * np.sqrt(T))
    return c_t, delta


def put(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    delta = norm.cdf(d1) - 1

    p_t = K * np.exp(-r * T) * norm.cdf(-(d1 - sigma * np.sqrt(T)))- S * (delta* -1)
    return p_t, delta


def calculate():
    # Obtém os valores dos parâmetros de entrada

    entrada_s =  s_entry.get().replace(",", ".")
    S = float(entrada_s)

    entrada_k = k_entry.get().replace(",", ".")
    K = float(entrada_k)

    T = float(t_entry.get())/365

    entrada_r = r_entry.get().replace(",", ".")
    r = float(entrada_r) / 100

    entrada_sigma = sigma_entry.get().replace(",", ".")
    sigma = float(entrada_sigma) / 100

    c, d_c = call(S, K, T, r, sigma)
    p, d_p = put(S, K, T, r, sigma)


    result_label.config(text=f"O preço da call é: R${c:.2f} \n O preço da put é: R${p:.2f} \n----------------------------\n Delta da call: {d_c*100:.0f}% \n Delta da put: {d_p*100:.0f}%" )

# Criar a janela
root = tk.Tk()
root.title("Calculadora de Opções")

# Criar um rótulo de título
title_label = tk.Label(root, text="Calculadora Black-Scholes - PNBY Capital", font=("Arial", 16), fg='blue')

# Organizar o rótulo na janela
title_label.grid(row=0, column=0, columnspan=4)

# Labels e Entries
s_label = tk.Label(root, text="Preço atual do ativo:")
s_label.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14
s_entry = tk.Entry(root)
s_entry.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14

k_label = tk.Label(root, text="Preço de exercício da opção(Strike): ")
k_label.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14
k_entry = tk.Entry(root)
k_entry.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14

t_label = tk.Label(root, text="Tempo até a expiração da opção (em dias) :")
t_label.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14
t_entry = tk.Entry(root)
t_entry.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14

r_label = tk.Label(root, text="Taxa de juros livre de risco (%a.a.) :")
r_label.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14
r_entry = tk.Entry(root)
r_entry.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14

sigma_label = tk.Label(root, text="Volatilidade do ativo (%a.a.) :")
sigma_label.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14
sigma_entry = tk.Entry(root)
sigma_entry.config(font=("Arial", 14))  # altera a fonte para Arial com tamanho 14

calc_button = tk.Button(root, text="Calcular", command=calculate, font=("Arial", 14), fg='blue')
result_label = tk.Label(root, text="", font=("Arial", 14), fg='red')


# Organização na janela
s_label.grid(row=2, column=0)
s_entry.grid(row=2, column=1)

k_label.grid(row=3, column=0)
k_entry.grid(row=3, column=1)

t_label.grid(row=4, column=0)
t_entry.grid(row=4, column=1)

r_label.grid(row=5, column=0)
r_entry.grid(row=5, column=1)

sigma_label.grid(row=6, column=0)
sigma_entry.grid(row=6, column=1)

calc_button.grid(row=7, column=1)

result_label.grid(row=9, column=0, columnspan=2)

# Iniciar o loop principal da janela

root.mainloop()


#caminho para criar executável
#pyinstaller --onefile -w C:\Users\nahta\PycharmProjects\projetos_pycharm\venv01\calculadora black scholes.py

#source C:/Users/nahta\PycharmProjects/projetos_pycharm/venv01/bin/activate#source C:/Users/nahta/PycharmProjects/projetos_pycharm/venv01/bin/activate


