import random

NUMBER_OF_REPEATS = 1000

PROBABILITY = 0.3

for n in [10, 100, 1000]:
    sum_of_heads = 0.0
    # here we do experiment of {flip a coin n times and count heads} 1000 times to reach the nearest value to reality
    for rep in range(NUMBER_OF_REPEATS):
        sum_of_heads += len([1 for _ in range(n) if random.uniform(0, 1) < PROBABILITY])
    print("n = ", n, "\t\tn * p = ", n * PROBABILITY, "\t\taverage of heads = ", sum_of_heads / NUMBER_OF_REPEATS)
