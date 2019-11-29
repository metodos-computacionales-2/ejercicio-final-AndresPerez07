import numpy as np
import matplotlib.pyplot as plt

rs = [0.5, 1.1, 2.1, 3.1, 3.5, 3.8]

fig = plt.figure(figsize=(15,10))
i = 1
for r in rs:
    data = np.loadtxt("datos-{}.txt".format(r))
    ax = fig.add_subplot(2,3,i)
    ax.plot(data[:,0],data[:,1], label="R={}".format(r))
    ax.set_xlim(-1,80)
    # ax.set_ylim(0.2,0.6)
    ax.legend()
    i += 1
plt.show()

#%%

x = np.linspace(0,1,100)

for r in rs:
    plt.plot(x,r*x*(1-x), label="R={}".format(r))
    plt.legend()

plt.show()
