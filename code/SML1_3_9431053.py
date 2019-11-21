import random

dice_n_times = [0] * 6
N = 1000

for _ in range(N):
    dice_n_times[random.randint(0, 5)] += 1

# Probabilities for the question:
p_a = float((dice_n_times[1] + dice_n_times[3] + dice_n_times[5]) / N)
p_b = float((dice_n_times[0] + dice_n_times[1] + dice_n_times[2] + dice_n_times[3]) / N)
p_ab = float((dice_n_times[1] + dice_n_times[2]) / N)
print("P(AB) =", p_ab, "\t,P(A) =", p_a, "\t,P(B) =", p_b, "\t,P(A) * P(B) =", p_a * p_b)

# Probabilities for the suggested events which event A is {1, 2, 3} and event B is {4, 5}
p_a = float((dice_n_times[0] + dice_n_times[1] + dice_n_times[2]) / N)
p_b = float((dice_n_times[3] + dice_n_times[4]) / N)
p_ab = 0
print("P(AB) =", p_ab, "\t\t,P(A) =", p_a, "\t,P(B) =", p_b, "\t,P(A) * P(B) =", p_a * p_b)
