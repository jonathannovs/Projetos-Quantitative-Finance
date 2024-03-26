import tkinter as tk
import numpy as np
import math
from scipy.stats import norm
from PIL import ImageTk, Image

def call(S, K, T, r, sigma_call):
    d1 = (np.log(S/K) + (r + sigma_call**2/2)*T) / (sigma_call*np.sqrt(T))
    delta = norm.cdf(d1)

    c_t = S * delta - K * np.exp(-r * T) * norm.cdf(d1 - sigma_call * np.sqrt(T))
    return c_t

def put(S, K, T, r, sigma_put):
    d1 = (np.log(S/K) + (r + sigma_put**2/2)*T) / (sigma_put*np.sqrt(T))
    delta = norm.cdf(d1) - 1

    p_t = K * np.exp(-r * T) * norm.cdf(-(d1 - sigma_put * np.sqrt(T)))- S * (delta* -1)
    return p_t

def calculate():
    # Obtém os valores dos parâmetros de entrada

    entrada_s =  s_entry.get().replace(",", ".")
    S = float(entrada_s)

    entrada_k = k_entry.get().replace(",", ".")
    K = float(entrada_k)

    t = float(t_entry.get())
    T = t/365

    entrada_r = r_entry.get().replace(",", ".")
    r = float(entrada_r) / 100

    entrada_sigma_call = sigma_call_entry.get().replace(",", ".")
    sigma_call = float(entrada_sigma_call) / 100

    entrada_sigma_put = sigma_put_entry.get().replace(",", ".")
    sigma_put = float(entrada_sigma_put) / 100

    entrada_choque = choque_entry.get().replace(",", ".")
    porc = float(entrada_choque)

    D = float(dia_entry.get())

    #chamando a função
    c = call(S, K, T, r, sigma_call)
    p = put(S, K, T, r, sigma_put)

    #Calculando o Delta da PUT com sua volatilidade especifica
    #d1_put = (np.log(S / K) + (r + sigma_put ** 2 / 2) * T) / (sigma_put * np.sqrt(T))
    #delta_put = (norm.cdf(d1_put) - 1) * np.exp(-r * T)


    #FÓRMULA PARA CÁLCULO DO CHOQUE EM % E EM DIAS DO ATIVO
    x_c = S*((porc/100)+1)     #multiplicando o Valor do ativo pela porcentagem que se quer do choque
    X_T = (t - D)/365          #Subraindo o D do t e criando uma nova variavel para ser usada no calculo do choque

    # calulando a call com os novos valores do choque
    d1_choque = (np.log(x_c / K) + (r + sigma_call ** 2 / 2) * X_T) / (sigma_call * np.sqrt(X_T))
    delta_choque = norm.cdf(d1_choque)
    call_choque = x_c * delta_choque - K * np.exp(-r * X_T) * norm.cdf(d1_choque - sigma_call * np.sqrt(X_T))
    x = call_choque

    # Calculando o DELTA da >>>>>>>CALL<<<<<< ja que seus valores dependem do choque
    d1_choque_x = (np.log(x_c / K) + (r + sigma_call ** 2 / 2) * X_T) / (sigma_call * np.sqrt(X_T))
    delta_call = norm.cdf(d1_choque_x)


    y_p = S*((porc/100)+1)   #multiplicando o Valor do ativo pela porcentagem que se quer do choque
    Y_T = (t - D) / 365      #Subraindo o D do t e criando uma nova variavel para ser usada no calculo do choque

    #calulando a put com os novos valores do choque
    d1_choque_y = (np.log(y_p / K) + (r + sigma_put ** 2 / 2) * Y_T) / (sigma_put * np.sqrt(Y_T))
    delta_choque_y = norm.cdf(d1_choque_y) - 1
    putt_choque = K * np.exp(-r * Y_T) * norm.cdf(-(d1_choque_y - sigma_put * np.sqrt(Y_T)))- y_p * (delta_choque_y* -1)
    y = putt_choque

    #Calculando o DELTA da >>>>>>PUT<<<<<<< ja que seus valores dependem do choque
    d1_choque_put = (np.log(y_p / K) + (r + sigma_put ** 2 / 2) * Y_T) / (sigma_put * np.sqrt(Y_T))
    delta_put = (norm.cdf(d1_choque_put) - 1) * np.exp(-r * Y_T)


    result_label.config(text=f"Preço da call: R${c:.2f} \n Preço da put: R${p:.2f} \n Delta da call: {delta_call*100:.0f}% \n Delta da put: {delta_put*100:.0f}% \n Choque de {porc}% e {D:.0f} dias da call: R${x:.2f} \n Choque de {porc}% e {D:.0f} dias da put: R${y:.2f} \n ")

##########################
def clear_entries():            #FUNÇÃO DA LIMPEZA
    s_entry.delete(0, 'end')
    k_entry.delete(0, 'end')
    t_entry.delete(0, 'end')
    r_entry.delete(0, 'end')
    choque_entry.delete(0, 'end')
    dia_entry.delete(0,'end')
    sigma_call_entry.delete(0, 'end')
    sigma_put_entry.delete(0, 'end')
    result_label.config(text="")

# Criar a janela
janela = tk.Tk()
janela.geometry("1100x700")
janela.title("Calculadora de opções")

# imagem de fundo
caminho_imagem_pnby = r'C:\Users\nahta\PycharmProjects\projetos_pycharm\venv01\Panamby_logo_4.jpg'
imagem = Image.open(caminho_imagem_pnby)
imagem_tk = ImageTk.PhotoImage(imagem)
label_imagem = tk.Label(janela, image=imagem_tk,bg='grey')
label_imagem.place(x=700, y=10)

# Criar um rótulo de título
title_label = tk.Label(janela, text="Calculadora Black-Scholes - PNBY Capital", font=("Arial 25"), fg='white',bg='grey')

# Organizar o rótulo na janela
title_label.grid(row=0, column=0, columnspan=4,pady=12,padx=12)

# Labels e Entries
s_label = tk.Label(janela, text="Preço atual do ativo:")
s_label.config(font=("Arial", 14),pady=3,padx=3)
s_entry = tk.Entry(janela)
s_entry.config(font=("Arial", 14),borderwidth=4)

k_label = tk.Label(janela, text="Preço de exercício da opção(Strike):",pady=8,padx=8)
k_label.config(font=("Arial", 14))
k_entry = tk.Entry(janela)
k_entry.config(font=("Arial", 14),borderwidth=4)

t_label = tk.Label(janela, text="Tempo até a expiração da opção (em dias corridos) :",pady=8,padx=8)
t_label.config(font=("Arial", 14))
t_entry = tk.Entry(janela)
t_entry.config(font=("Arial", 14),borderwidth=4)

r_label = tk.Label(janela, text="Taxa de juros livre de risco (%a.a.) :",pady=8,padx=8)
r_label.config(font=("Arial", 14))
r_entry = tk.Entry(janela)
r_entry.config(font=("Arial", 14),borderwidth=4)

sigma_call_label = tk.Label(janela, text="Volatilidade da call (%a.a.) :" ,pady=8,padx=8)
sigma_call_label.config(font=("Arial", 14))
sigma_call_entry = tk.Entry(janela)
sigma_call_entry.config(font=("Arial", 14),borderwidth=4)

sigma_put_label = tk.Label(janela, text="Volatilidade da put (%a.a.) :" ,pady=8,padx=8)
sigma_put_label.config(font=("Arial", 14))
sigma_put_entry = tk.Entry(janela)
sigma_put_entry.config(font=("Arial", 14),borderwidth=4)

choque_label = tk.Label(janela, text="Choque do ativo (%) :" ,pady=8,padx=8)
choque_label.config(font=("Arial", 14))
choque_entry = tk.Entry(janela)
choque_entry.config(font=("Arial", 14),borderwidth=4)

dia_label = tk.Label(janela, text="Choque em dias do ativo: ",pady=10,padx=10)
dia_label.config(font=("Arial", 14))
dia_entry = tk.Entry(janela)
dia_entry.config(font=("Arial", 14),borderwidth=4)

calc_button = tk.Button(janela, text="Calcular", command=calculate,font=("Arial", 14), fg='white', bg='blue',borderwidth=9)

###################  BOTÃO DA LIMPEZA
clear_button = tk.Button(janela, text="Limpar", command=lambda: clear_entries())
clear_button.config(font=("Arial", 14), bg='red', fg='white',borderwidth=5)
#######################

result_label = tk.Label(janela, text="", font=("Arial BOLD", 18), fg='yellow',bg='black')

# Organização na janela
s_label.grid(row=5, column=0)
s_entry.grid(row=5, column=1)

k_label.grid(row=6, column=0)
k_entry.grid(row=6, column=1)

t_label.grid(row=7, column=0)
t_entry.grid(row=7, column=1)

r_label.grid(row=8, column=0)
r_entry.grid(row=8, column=1)

sigma_call_label.grid(row=9, column=0)
sigma_call_entry.grid(row=9, column=1)

sigma_put_label.grid(row=10, column=0)
sigma_put_entry.grid(row=10, column=1)

choque_label.grid(row=11, column=0)
choque_entry.grid(row=11, column=1)

dia_label.grid(row=12, column=0)
dia_entry.grid(row=12, column=1)

calc_button.grid(row=13, column=1)

result_label.grid(row=14, column=0, columnspan=2)

clear_button.grid(row=13, column=0,columnspan=2, pady=9, padx=2)

# Iniciar o loop principal da janela

janela.mainloop()

#caminho do executável
#pyinstaller --onefile -w C:\Users\nahta\PycharmProjects\projetos_pycharm\venv01\calculadora_V1.py
#pyinstaller --onefile -w --add-data "C:\Users\nahta\PycharmProjects\projetos_pycharm\venv01\Panamby_logo_4.jpg;." calculadora_V1.py (adicionar imagem ao exe.)
