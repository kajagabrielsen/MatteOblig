import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametere
Lx, Ly = 1, 1  # størrelse på griden
Nx, Ny = 50, 50  # gridpunkter
Nt = 100  # tidstep
dt = 0.0001 
T = 0.05
k = T/Nt
hx = Lx/Nx
hy = Ly/Ny
alphax = k / hx**2  # termisk diffusivitet (k/h^2), hvor raskt varmen sprer seg i materialet
alphay = k / hy**2

#bestemmer initialbetingelser
def initialbet(x, y):
    return np.sin(np.pi * x) * np.sin(np.pi * y)

# setter opp grid
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

u = initialbet(X, Y)

# Eksplisitt metode med u som matrisen som inneholder temperaturfordelingen
for n in range(Nt):
    u_new = u.copy()
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u_new[i, j] = u[i, j] + (
                alphax*(u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) +
                alphay*(u[i, j + 1] - 2 * u[i, j] + u[i, j - 1])
            )*dt

    u = u_new


# Plotter resultatet
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, u, cmap='hot_r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Temperatur')
ax.set_title('Varmelikningen i 2D')
plt.show()