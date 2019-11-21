import numpy as np

MEAN = [0, 0]
COVARIANCE = [[1.0, 0.5], [0.5, 0.333333333]]
NUMBER_OF_SAMPLES = 1000
x, y = np.random.multivariate_normal(MEAN, COVARIANCE, NUMBER_OF_SAMPLES).T
print('covariance is:\n', np.cov(x, y))
print('average is:', np.average((x, y)))
