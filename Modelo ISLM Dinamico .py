"""
@author: Gustavo Asaph Dilay de Paula
"""

'''Importação de bibliotecas, declaração de Variáveis exógenas e Parâmetros
    e declaração de listas para armazenar as variáveis dinâmicas '''


import numpy as np               
import math as ma                
import pandas as pd              
import matplotlib.pyplot as plt  

"Exemplos de variáveis exógenas"
C0 = 500             # consumo autonomo
c  = 0.8             # propensão marginal a consumir
I0 = 400             # investimento - fixo ou contstante
G  = 200             # Gasto do governo - fixo ou constante
T  = 200             # trinutos - fixo ou constante
k  = 0.4
h  = 9000
M  = 1500
d = 0.10
f = 9000
Y  = []              # Lista para armazenar os valores de Y(t), no tempo
C  = []              # Lista para armazenar os valores de C(t), no tempo 
D  = []              # Lista para armazenar Divida do governo
I = []
i = []
m  = 1/(1-c)         # multiplicador simples da Curva IS
time = 31


'''
    Equações dinâmicas   
'''
#Equação Renda    
def eqY():
    _y = C[t] + I0 + G
    Y.append(_y)

#Equação Consumo   C = C0 + c(Y(t-1) - T)
def eqC(_RendaAnterior):                      
    _c = C0 + c*(_RendaAnterior-T)            
    C.append(_c)                           

#Equação Investimento
def eqI():
    _I = I0 +d*Y[t-1] - f*i[t-1]
    I.append(_I)
    

  
#Equação Dívida
def eqD(_DivAnterior):
    _d = _DivAnterior + T - G
    D.append(_d)

#Equação Taxa de Juros
def eqi():
   _i = Y[t]*k/h - M*1/h
   i.append(_i)
   

'''
    Calculos iterados no tempo após um 
    aumento permanente dos gastos do governo G = 220
'''
# Inicia vetores em t=0, com valores iniciais (condições iniciais)
y_eq = (1/(1-c))*(C0+I0 + G -c*T)
i_eq = k/h*y_eq - 1/h*M
c_eq = C0+c*(y_eq - T)
I_eq = I0 + d*y_eq - f*i_eq
Y.append(y_eq)                    
i.append(i_eq)
C.append(c_eq)
I.append(I_eq)
D.append(T-G)

"EXEMPLO"
G = 220                   # choque de política fiscal: aumento permanente de G




'''
     Loop temporal (cria série temporal para cada variavel endógena)
'''
for t in range(1,time):
    eqC(Y[t-1])          # Introdução da defasagem temporal
    eqI()
    eqY()                
    eqi()
    eqD(D[t-1])
    

    
'''    
     Resultados
'''
Y
i 
C
I
D

zip(Y,C,D)               # junta as lista numa única tabela
list(zip(Y,C,D))
df = pd.DataFrame(list(zip(Y,C,D)),columns =['Y', 'C','D'])
df.to_csv("ModISLM-ResultX.csv")


'''
     Gráficos
'''
t = list(range(0,time))
plt.plot(t,Y,label="Y(t)",color="blue")    
plt.plot(t,C,label="C(t)",color='red')    
plt.plot(t,I,label="I(t)",color='black')  
plt.plot(t,D,label="D(t)",color='red') 
plt.plot(t,i,label="i(t)",color='orange')   

'''
     Gráficos Reunidos
'''
figure, axis = plt.subplots(2, 3,constrained_layout=True)
# Renda
axis[0, 0].plot(Y,label="Y(t)",color="blue")    
axis[0, 0].set_title("Y(t)")
# Consumo
axis[0, 1].plot(C,label="C(t)",color='red')
axis[0, 1].set_title("C(t)")
# Dívida
axis[1, 0].plot(D,label="D(t)",color='black')
axis[1, 0].set_title("D(t)")
# Taxa de Juros
axis[1, 1].plot(i,label="i(t)",color='orange')
axis[1, 1].set_title("i(t)")
#Investimento
axis[1, 2].plot(I,label="I(t)",color='black')
axis[1, 2].set_title("I(t)")
