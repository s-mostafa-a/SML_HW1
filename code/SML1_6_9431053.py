import numpy as np
import matplotlib.pyplot as plt
import random

SAMPLES = 1000


def binomial(n, p):
    return np.asarray([len([1 for _ in range(n) if random.uniform(0, 1) < p]) for __ in range(SAMPLES)])


X1 = binomial(100, 0.3)
X2 = binomial(100, 0.5)
X3 = binomial(200, 0.5)
X1_plus_X2_equivalent = binomial(100, 0.8)
X2_plus_X3_equivalent = binomial(300, 0.5)

plt.subplot(211).set_title("real X1 + X2")
plt.hist(np.add(X1, X2))
plt.subplot(212).set_title("the binomial equivalent to X1 + X2")
plt.hist(X1_plus_X2_equivalent)
plt.show()
print('average of real X1 + X2:', np.average(np.add(X1, X2)))

plt.subplot(211).set_title("real X2 + X3")
plt.hist(np.add(X2, X3))
plt.subplot(212).set_title("the binomial equivalent to X2 + X3")
plt.hist(X2_plus_X3_equivalent)
plt.show()
print('average of real X2 + X3:', np.average(np.add(X2, X3)))
