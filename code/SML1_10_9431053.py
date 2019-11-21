import numpy as np
import matplotlib.pyplot as plt
import math
import random

SAMPLES = 1000


def binomial(n, p):
    return np.asarray([len([1 for _ in range(n) if random.uniform(0, 1) < p]) for __ in range(SAMPLES)])


LAM = 6
N = 20
Xs = list(range(N))
Ys = np.asarray([(((math.e ** (-LAM)) * (LAM ** k)) / (math.factorial(k))) for k in Xs])
Xs = np.asarray(Xs)
plt.subplot(211).set_title("poisson")
plt.plot(Xs, Ys)

binom = binomial(100, 0.06)
plt.subplot(212)
ax = plt.subplot(212)
ax.set_title("binomial")
plt.hist(binom, bins=20, range=[0, 20])

plt.show()
print('binomial average: ', np.average(binom))
poisson_average = np.sum(np.asarray([x * Ys[x] for x in Xs])) / np.sum(np.asarray([Ys[x] for x in Xs]))
print('poisson average: ', poisson_average)
