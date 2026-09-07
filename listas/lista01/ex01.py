import numpy as np
import matplotlib.pyplot as plt

# declarando a funcao e as amostras
t = np.linspace(0, 1, num=20)
conjunto = 1 + np.sin(2 * np.pi * t)

# plot
plt.plot(t, conjunto, label='1 + sin(2πt) V', color='pink')

plt.xlabel('amostras')
plt.ylabel('conjunto')
plt.title('1 + sin(2πt) V')
plt.legend()
plt.show()