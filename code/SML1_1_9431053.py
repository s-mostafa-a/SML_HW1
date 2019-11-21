import random
import matplotlib.pyplot as plt

NUMBER_OF_TESTS = [10, 20, 50, 75, 100, 150, 200, 300, 500, 700, 1000]


def do_test(probability, subplt):
    heads = len([1 for _ in range(NUMBER_OF_TESTS[-1]) if random.uniform(0, 1) < probability])
    print('result probability from tests with n =', NUMBER_OF_TESTS[-1], 'and p =', probability, 'is:',
          float(float(heads) / float(NUMBER_OF_TESTS[-1])))

    result_probabilities_from_tests = []
    for n in NUMBER_OF_TESTS:
        heads = len([1 for _ in range(n) if random.uniform(0, 1) < probability])
        result_probabilities_from_tests.append(float(float(heads) / float(n)))
    plt.subplot(subplt).set_title(str(probability))
    plt.plot(NUMBER_OF_TESTS, result_probabilities_from_tests, '-')
    plt.axis([0, 1000, 0, 1])


do_test(0.3, 211)
do_test(0.03, 212)
plt.show()
