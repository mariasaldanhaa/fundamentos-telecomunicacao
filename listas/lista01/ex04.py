import numpy as np
import matplotlib.pyplot as plt
from ex02 import tensaoNivel, t

# os índices de uma lista começam em 0,
# já que o último número do meu RA é 2, 
# então o segundo elemento é a posição 1.
 
# Segunda amostra: 1011
# Trocando um dos quatro bits:
# 1011 -> 1010, alterei o último bit, o qual estava 1 e alterei para 0

decimal = int("1010", 2)
tensaoAlterada = decimal * 0.125
tensaoNivelOriginal = tensaoNivel.copy()
tensaoNivel[1] = tensaoAlterada

plt.figure(figsize=(8, 4))

# sinal original - Q2b
plt.step(t, tensaoNivelOriginal, where='post', label='Original -Q2b', color='blue')

# sinal alterado - Q4
plt.step(t, tensaoNivel, where='post', label='Alterado - Q4', color='red')

# plot 
plt.xlabel('Tempo contínuo')
plt.ylabel('Valores de tensão correspondentes aos níveis (em Volts)')
plt.title('Comparação: sinal original x sinal com perturbação na 2ª amostra')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()