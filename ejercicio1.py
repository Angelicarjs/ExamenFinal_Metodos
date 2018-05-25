# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

#fx[i+1] - fx[i] / x[i+1] - x[i] si fuera con un ciclo 

der1 = fx[1:] - fx[:-1] / (x[1:] - x[:-1]) # primera derivada usando el punto de atras se pierde el primer punto

der2 = der1[1:] - der1[:-1] / (x[2:] - x[:-2]) #segunda derivada usando el punto de atras se pierde los dos primeros puntos

