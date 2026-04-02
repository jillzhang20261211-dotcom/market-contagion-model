#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

T = 1.0
N = 1000
dt = T / N

mu = 0.05
sigma = 0.2
alpha = 0.5
m = 1.0

S = np.zeros(N)
S[0] = 100

J = 0.0

def f(x):
    return 1 - np.exp(-x)

for t in range(1, N):
    dW = np.sqrt(dt) * np.random.randn()
    J += abs(dW)
    contagion = f(max(J - m, 0))
    S[t] = S[t-1] * (1 + mu*dt + sigma*dW + alpha*contagion*dt)

plt.plot(S)
plt.title("Threshold-Driven Market Contagion Model")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()

