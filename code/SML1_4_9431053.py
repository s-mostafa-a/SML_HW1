import random


def one_round(change):
    goal = random.randint(0, 2)
    choose = random.randint(0, 2)
    if not change:
        if goal is choose:
            return True
        else:
            return False
    if change:
        if goal is choose:
            return False
        else:
            return True


N = 1000
win_without_change = 0
for i in range(N):
    win_without_change += 1 if one_round(False) else 0
print("winning probability with no change:", float(win_without_change / N))

win_with_change = 0
for i in range(0, N):
    win_with_change += 1 if one_round(True) else 0
print("winning probability with change:", float(win_with_change / N))
