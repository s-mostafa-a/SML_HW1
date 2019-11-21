import numpy as np
import matplotlib.pyplot as plt


def draw_cdf(data, subplot, label):
    num_bins = 20
    counts, bin_edges = np.histogram(data, bins=num_bins, normed=True)
    cdf = np.cumsum(counts)
    plt.subplot(subplot).set_title(label)
    bin_edges = bin_edges / bin_edges[len(bin_edges) - 1]
    plt.plot(bin_edges[1:], cdf)


samples = 10000
subplt_suffix = 1
for i in (1, 100, 1000, 10000):
    draw_cdf(np.random.normal(0, float(1 / i), samples), 410 + subplt_suffix, 'variance: ' + str(float(1 / i)))
    subplt_suffix += 1
plt.show()
