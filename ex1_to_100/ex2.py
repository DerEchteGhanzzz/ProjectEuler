def get_exercise_number():
    return 2

def solve():
    total = 0
    fib_1 = 1
    fib_2 = 2
    while fib_2 <= 4*10**6:
        if fib_2 % 2 == 0:
            total += fib_2

        fib_3 = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_3

    return total