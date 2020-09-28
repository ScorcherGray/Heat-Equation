import numpy as np
import matplotlib.pyplot as plt

t_range = list(range(11))
h = 0.03
alpha_gold = 0.1 #127 * 10 ** -16
dt_max = h**2/(4*alpha_gold) # <= h**2/(4 * alpha) > 0
dt = h**2/(4.5*alpha_gold)

if dt > dt_max:
    print("error: dt greater than max allowed value")

x = np.arange(-1,1,h)
y = np.arange(-1,1,h)
X, Y = np.meshgrid(x,y)

T = X*0
#T[(np.abs(X)< 0.2) & (np.abs(Y) < 0.2)] = 1 #Square
T[(np.abs(X**2 + Y**2) < 0.2) & (np.abs(X**2 + Y**2) < 0.4)] = 1 #circle
#T[(np.abs(2*X) < 0.2) & (np.abs(Y) < 0.2)] = 1 # rectangle
#T[(np.abs(Y - X**2) < 0.2)] = 1 # Parabola
#T[(np.abs(X*Y) < 0.1)] = 1 # Starburst
Tarray = []
Tarray.append(T)

for time in range(51):
    nextT = T.copy()
    for i in range(1,len(X)-1):
        for j in range(1, len(Y)-1):
            nextT[i,j] = (1 - 4*dt*alpha_gold/h**2)*Tarray[-1][i][j] + dt*alpha_gold*(Tarray[-1][i][j-1] + \
                Tarray[-1][i-1][j] + Tarray[-1][i+1][j] + Tarray[-1][i][j+1])/h**2

    Tarray.append(nextT)

stepsArray = [0, 1, 2, 3, 4, 7, 10, 50]
fig, ax = plt.subplots(nrows=2, ncols=4)
i = 0
for steps in stepsArray:
    col = i%4
    row = int(i/4)
    ax[row][col].pcolormesh(X, Y, Tarray[steps], cmap = 'jet', vmin=0, vmax = 1)
    ax[row][col].title.set_text("{} time steps".format(steps))
    ax[row][col].axis('off')
    i += 1

plt.axis('off')
plt.show()