import numpy as np
import matplotlib.pyplot as plt
import os
from funcion_n import suma, resta, multiplicacion

resultado1 = suma(4, 5)
resultado2 = resta(24, 9)
resultado3 = multiplicacion(10, 6)
resultado4 = resta(1, 6)

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y, label='y = x^2')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfica x")
plt.legend()
plt.grid()

nombre_carpeta = "resultados"

ruta_png = os.path.join(nombre_carpeta, "grafica1.png")
ruta_eps = os.path.join(nombre_carpeta, "grafica1.eps")

plt.savefig(ruta_png, dpi=300)
plt.savefig(ruta_eps)

print(f"Gráficas guardadas en la carpeta: {nombre_carpeta}")
