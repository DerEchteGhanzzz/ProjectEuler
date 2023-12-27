def get_exercise_number():
    return 3


def solve(n=600851475143):
    i = 2
    while i <= n:
        if n % i == 0:
            if n // i == 1:
                return n
            new_n = n // i
            return solve(new_n)
        i += 1
