#code for showing the naive approach doesn't work 1

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, P.
P = 10 * 10**6
# Percentage of opulation who are open to revolting, N. (based on age, political inclination, medical history etc.)
N=P*(1/5)
# Initial number of exposed, infected and recovered individuals, E0, I0 and R0.
E0, I0, R0 = 0, 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 -E0
# Contact rate, beta, activation rate, gamma, and mean removal rate, alpha, (in 1/days).
beta = 1
alpha = 1./300
gamma = 1./5

# A grid of ticks
t_max=10
ticks_per_day=10000
t = np.linspace(0, t_max, t_max*ticks_per_day)

# Define transfer rate g(x)
# k is the threshold, n is the severity of the threshold, delta is the percentage of 'zealots'
k=3/50
n=2
delta=0.00
def g(x):
    y = delta+ gamma * ((x) ** n) / (k ** n + (x) ** n)
    return y

#having a freakishly large gamma allows there to be a revolution
#but it doesn't much look like one
#gamma = k*(N*2)

# The SIR model differential equations.
def SEIR_eq(y, t, N, beta, gamma, alpha):
    S, E, I, R = y
    Sdot = -beta * S * I
    Edot = beta * S * I - E * g(I/N)
    Idot = E * g(I/N) - alpha * I
    Rdot = alpha * I
    return Sdot, Edot, Idot, Rdot

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(SEIR_eq, y0, t, args=(N, beta, gamma, alpha))
S, E, I, R = ret.T

# Plot the data
# colours
s_colour='#ADD694'
e_colour='#FFCD47'
i_colour='#F2728C'
r_colour='#67B8C7'
# s_colour='Green'
# e_colour='Yellow'
# i_colour='Red'
# r_colour='Blue'

fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='w', axisbelow=True)
# ax.set_axis_bgcolor('white')
ax.plot(t, S, alpha=0.8, lw=4, label='Susceptible', color=s_colour)
ax.plot(t, E, alpha=0.8, lw=2, label='Exposed', color=e_colour)
ax.plot(t, I, alpha=0.8, lw=2, label='Infected', color=i_colour)
ax.plot(t, R, alpha=0.8, lw=2, label='Removed', color=r_colour)
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Number of Individuals')
ax.set_xlim(0)
ax.set_ylim(0,N*1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='black', lw=1, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.9)
# for spine in ('top', 'right'):
#     ax.spines[spine].set_visible(False)
# parameter_text = 'alpha=%s, beta=%s, gamma=%s, delta=%s, k=%s, n=%s, N=%s' % \
#                      ('%.4f' % alpha, '%.4f' % beta, '%.2f' % gamma, '%.2f' % delta, '%.2f' % k, '%.1f' % n, N)
# plt.text(t_max/20, N*1.1, parameter_text,
    #bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
plt.show()