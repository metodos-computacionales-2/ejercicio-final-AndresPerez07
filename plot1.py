import numpy as np
import matplotlib.pyplot as plt

Fd = ['1.350', '1.440', '1.465', '1.770']
p = []
for f in Fd:
    p.append(np.loadtxt("data_{}000.dat".format(f)))
p_delta = []
for f in Fd:
    p_delta.append(np.loadtxt("data_{}000_delta.dat".format(f)))

#%%

fig1 = plt.figure(figsize=(15,15))
for i in range(4):
    ax = fig1.add_subplot(2,2,i+1)
    ax.plot(p[i][:,0],p[i][:,1], label="Fd={}".format(Fd[i]))
    ax.set_xlabel("$time$")
    ax.set_ylabel(u"$\theta$")
    ax.legend()
plt.savefig("theta_vs_time.png")

#%%

fig2 = plt.figure(figsize=(15,15))
for i in range(4):
    ax = fig2.add_subplot(2,2,i+1)
    ax.scatter(p[i][:,1],p[i][:,2], s=5, label="Fd={}".format(Fd[i]))
    ax.set_xlabel(u"$\theta$")
    ax.set_ylabel("$\omega$")
    ax.legend()
plt.savefig("omega_vs_theta.png")

#%%

fig3 = plt.figure(figsize=(15,15))
for i in range(4):
    ax = fig3.add_subplot(2,2,i+1)
    ax.semilogy(p[i][:,0],np.abs(p_delta[i][:,1] - p[i][:,1]),marker="+", label="Fd={}".format(Fd[i]))
    ax.set_xlabel(u"$time$")
    ax.set_ylabel("$\Delta\Theta$")
    ax.legend()
plt.savefig("lyapunov.png")
#%%

bifurcacion = np.loadtxt("bifurcacion.dat")

#%%

fig4 = plt.figure(figsize=(15,15))
ax = fig4.add_subplot(111)

ax.scatter(bifurcacion[:,0], bifurcacion[:,1], marker=".", s=1)
ax.set_title("Diagrama de Bifurcación")
ax.set_ylim(1,3)

plt.savefig("bifurcacion.png")
