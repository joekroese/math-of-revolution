import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of exposed, infective and recovered individuals, E0, I0 and R0.
E0, I0, R0 = 0, 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 -E0
# Contact rate, beta, and mean recovery rate, alpha, (in 1/days).
beta = 0.0002
alpha = 1./10
gamma = 6./100
# A grid of ticks
t = np.linspace(0, 450, 450)

# The SIR model differential equations.
def SIR_eq(y, t, N, beta, gamma, alpha):
    S, E, I, R = y
    Sdot = -beta * S * I
    Edot = beta * S * I - gamma * E
    Idot = gamma * E - alpha * I
    Rdot = alpha * I
    return Sdot, Edot, Idot, Rdot

# Initial conditions vector
y0 = S0, E0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(SIR_eq, y0, t, args=(N, beta, gamma, alpha))
S, E, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t)
#
s_colour='#ADD694'
e_colour='#FFCD47'
i_colour='#F2728C'
r_colour='#67B8C7'
# s_colour='Green'
# e_colour='Yellow'
# i_colour='Red'
# r_colour='Blue'


fig = plt.figure(facecolor='#dddddd')
ax = fig.add_subplot(111, axis_bgcolor='w', axisbelow=True)
ax.plot(t, S, 'b', alpha=0.8, lw=2, label='Susceptible', color=s_colour)
ax.plot(t, E, 'b', alpha=0.8, lw=2, label='Exposed', color=e_colour)
ax.plot(t, I, 'r', alpha=0.8, lw=2, label='Infective', color=i_colour)
ax.plot(t, R, 'g', alpha=0.8, lw=2, label='Removed', color=r_colour)
ax.set_xlabel('Time (Days)')
ax.set_ylabel('Number of Individuals')
ax.set_xlim(0)
ax.set_ylim(0,N*1.1)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='black', lw=1, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.9)
for spine in ('top', 'right'):
    ax.spines[spine].set_visible(False)
plt.show()