import numpy as np
import random


def get_sum_of_heads_in_list_for_each_iteration(n, p):
    return np.asarray(
        [float(len([1 for _ in range(n) if random.uniform(0, 1) < p]) / float(n)) for __ in range(ITERATIONS)])


def do_experiment(p):
    data = get_sum_of_heads_in_list_for_each_iteration(N, p)
    counter = len([1 for i in data if (i < p - EPSILON or i > p + EPSILON)])
    print('for p:', p)
    print('counter:', counter)
    print('percent of whole iterations', float(counter / len(data)))
    print()


ITERATIONS = 100000
N = 100
EPSILON = 0.2

do_experiment(0.3)
do_experiment(0.5)
