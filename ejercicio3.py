#Ejercicio3
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# Grafique las dos series de datos en una misma imagen 'serie.png'
# Calcule la covarianza entre `u` y `v` e imprima su valor.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([12.,45.,6.,78.,34.,22.,-10.,31.,-27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

#Grafica de las series 
plt.figure()
plt.scatter(t,v)
plt.scatter(t,u)
plt.savefig('serie.png')

#inicializa matriz de covarianza 
cov = np.array([0,0] [0,0])

u_prom = np.sum(u)/ len(u)
v_prom = np.sum(v) / len(v)

#Covarianza
for i in range(len(u)):
    for j in range(len(u)):
        cov[i,j] = ((u[i]- u_prom)*(v[i]- v_prom))/ (len(u)-1)

