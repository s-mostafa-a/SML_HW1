import numpy as np
import math

MU = 3
SIGMA = math.sqrt(16)
N = 10000
SAMPLES = np.random.normal(MU, SIGMA, N)
SAMPLES = np.sort(SAMPLES)

# a: P(x < 7):
less_than_sevens = len([1 for i in SAMPLES if i < 7])
print('P(x < 7): ', float(less_than_sevens / N))

# b: P(x > -2):
more_than_minus_twos = len([1 for i in SAMPLES if i > -2])
print('P(x > -2): ', float(more_than_minus_twos / N))

# c: {x; P(X > x) = 0.05}
alpha = 1 - 0.05
index = int(N * alpha)
x = SAMPLES.item(index)
print('{x; P(X > x) = 0.05 } : {' + str(x) + '}')

# d: P(-2 <= x <= 2)
counter = 0
between_two_and_minus_twos = len([1 for i in SAMPLES if -2 < i < 2])
print('P(-2 <= x <= 2): ', float(between_two_and_minus_twos / N))

# e: P(0 <= x <= 4)
between_zero_and_fours = len([1 for i in SAMPLES if 0 < i < 4])
print('P(0 <= x <= 4): ', float(between_zero_and_fours / N))

# e: {x; P(|X|>|x|) = 0.05}
absolute_samples = np.fabs(SAMPLES)
absolute_samples = np.sort(absolute_samples)
alpha = 1 - 0.05
index = int(N * alpha)
x = absolute_samples.item(index)
print('{x; P(|X| > |x|) = 0.05} : {' + str(x) + '}')
