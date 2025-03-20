import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

#Creazione dei dati
n = 20
x = np.sin(np.linspace(0, 2*np.pi, n))
y = np.cos(np.linspace(0, 2*np.pi, n))
z = np.linspace(0, 1, n)

#Creazione dl grafico
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.stem(x, y, z)

# Aggiungere un titolo e etichette sugli assi
ax.set_title('Grafico 3D')
ax.set_xlabel('Asse X')
ax.set_ylabel('Asse Y')
ax.set_zlabel('Asse Z')

# Aggiungere una griglia
ax.grid(True)

# Modificare la vista 3D
ax.view_init(elev=20, azim=30)  # Cambiare l'angolo di visualizzazione


#Rimuove le etichette negli assi
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
