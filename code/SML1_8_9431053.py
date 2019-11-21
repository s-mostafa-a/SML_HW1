# done
import numpy as np
import matplotlib.pyplot as plt

SAMPLES = 1000
X = np.random.uniform(0, 1, SAMPLES)
Y = np.random.uniform(0, 1, SAMPLES)

plt.subplot(211).set_title('X-Y distribution')
plt.hist(np.subtract(X, Y))
plt.subplot(212).set_title('X/Y distribution')
plt.hist(np.divide(X, Y), bins=SAMPLES)
plt.show()
