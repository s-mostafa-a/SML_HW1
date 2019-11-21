import matplotlib.pyplot as plt
import numpy as np


def show_sample_mean_plot(samples_of_distribution, subplt, label):
    sum_of_samples_to_i = 0
    n = len(samples_of_distribution)
    sample_mean = []
    for i in range(n):
        sum_of_samples_to_i += float(samples_of_distribution[i])
        sample_mean.append(float(sum_of_samples_to_i / float(i + 1)))
    other_axis = np.asarray(list(range(1, n + 1)))
    plt.subplot(subplt).set_title(label)
    plt.plot(other_axis, sample_mean, 'b')


# normal distribution:
MU = 0
SIGMA = 1
N = 10000
samples = np.random.normal(MU, SIGMA, N)
show_sample_mean_plot(samples, 211, "Normal distribution's sample mean")

# cauchy
samples = np.random.standard_cauchy(N)
show_sample_mean_plot(samples, 212, "Cauchy distribution's sample mean")

plt.show()
