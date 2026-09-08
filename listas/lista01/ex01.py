import numpy as np
import matplotlib.pyplot as plt

# declarando a funcao e as amostras
t = np.linspace(0, 1, num=20)
conjunto = 1 + np.sin(2 * np.pi * t)

# sample and hold
plt.figure(figsize=(8, 4)) # indica o tamanho da figura
plt.step(t, conjunto, where='post', label='Sample & Hold', linewidth=2)

# plot
plt.plot(t, conjunto, label='Linha contínua', color='pink')

plt.xlabel('amostras')
plt.ylabel('conjunto')
plt.title('1 + sin(2πt) V')
plt.grid(True) # coloca grade no fundo do gráfico
plt.tight_layout() # organiza os elementos para não ficarem cortados
plt.legend()
plt.show()