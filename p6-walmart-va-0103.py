import matplotlib.pyplot as plt
import numpy as np
# Santiago Medrano NC 0103 

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos,precio)
plt.show()

# personalizar graficas
plt.plot(cant_productos,precio,color='green',marker='*',linestyle='dashed',linewidth=2,markersize=12 )
plt.title("Venta de walmart")
plt.xlabel("cantidad productos")
plt.ylabel("precios")
plt.show()

# 