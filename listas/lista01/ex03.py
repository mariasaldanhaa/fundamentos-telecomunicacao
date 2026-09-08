import numpy as np
from ex02 import niveisQuantizacao

conversaoBinario = np.array([np.binary_repr(num, 4) for num in niveisQuantizacao])
concatenacao = "".join(conversaoBinario)

print(concatenacao)
# resultado: 
# 10001011110111111111111111111110110010010111010000100001000000000001001101011000