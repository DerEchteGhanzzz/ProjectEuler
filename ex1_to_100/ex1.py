def get_exercise_number():
    return 1


def solve():
    threes = 0
    fives = 0
    for i in range(1000):
        if i % 3 == 0:
            threes += i
        elif i % 5 == 0:
            fives += i
    return threes + fives
