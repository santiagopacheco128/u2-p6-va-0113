import matplotlib.pyplot as ptl
import numpy as np

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 18000]

# Gráfica básica
ptl.plot(cant_productos, precio)
ptl.show()

# Personalizar gráfica
ptl.plot( cant_productos,precio,color="green",marker="o",linestyle="dashed",linewidth=2, markersize=12)
ptl.title("ventas de walmart")
ptl.xlabel("cant prod")
ptl.ylabel("precios")
ptl.show()