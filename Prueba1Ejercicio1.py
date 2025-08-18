import numpy as np
matriz = np.random.randint(1, 101, size=(4, 4))
print(matriz)
submatriz = matriz[:2, 2:]
print(submatriz)

import matplotlib.pyplot as plt
matriz = np.random.randint(1, 101, size=(4, 4))

#Gráfico
x = np.arange(len(matriz[0]))
y = matriz[0]
plt.plot(x, y, label='Primera fila', linestyle='dashed',color='green')
plt.title('Primera fila de la matriz')
plt.xlabel('Índice de columna')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma
matriz = np.random.randint(1, 101, size=(4, 4))
plt.figure(figsize=(7,5))
plt.hist(matriz.flatten(), bins=30, color="black", edgecolor="red", alpha=0.8)
plt.title("Histograma de Datos normales")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.grid(axis="y", alpha=0.75)
plt.show()

