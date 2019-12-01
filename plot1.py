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
    # ax.set_ylim(0.0,0.4)
    ax.legend()
    i += 1
plt.show()

#%%

x = np.linspace(0,1,100)

for r in rs:
    plt.plot(x,r*x*(1-x), label="R={}".format(r))
    plt.legend()

plt.show()
#%%

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
    ax.semilogy(p[i][:,0],p_delta[i][:,1] - p[i][:,1],marker="+", label="Fd={}".format(Fd[i]))
    ax.set_xlabel(u"$time$")
    ax.set_ylabel("$\Delta\Theta$")
    ax.legend()
plt.savefig("lyapunov.png")
