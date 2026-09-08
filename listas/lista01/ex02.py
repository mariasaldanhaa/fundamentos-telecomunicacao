import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, num=20)
conjunto = 1 + np.sin(2 * np.pi * t)

# tamanho de cada nível:
# Vref = 2V
# Usa 4 bits para descobrir a quantidade de níveis, então: 2**4 = 16
# tamanho de cada nível => tamanho = Vref / qtd. níveis
# 2 / 16 = 0.125
tamanhoNivel = 0.125

niveisQuantizacao = np.round(conjunto / tamanhoNivel).astype(int)
niveisQuantizacao = np.clip(niveisQuantizacao, 0, 15) ## importante para a questão 3

# plot gráfico A
plt.step(t, niveisQuantizacao, where='post')
plt.xlabel('Tempo contínuo')
plt.ylabel('Níveis de quantização')
plt.title('Gráfico A - Níveis de Quantização')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

# plot gráfico B
tensaoNivel = niveisQuantizacao * tamanhoNivel
plt.step(t, tensaoNivel, where='post')
plt.xlabel('Tempo contínuo')
plt.ylabel('Valores de tensão correspondentes aos níveis (em Volts)')
plt.title('Gráfico B - Valores de tensão em cada nível')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()