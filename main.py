import time
from ex1_to_100 import ex1, ex2, ex3, ex4, ex5, ex6, ex7


def solve(ex):
    start = time.time_ns()
    answer = ex.solve()
    finish = time.time_ns()
    print(f"Ex. {ex.get_exercise_number()}: {answer} in {(finish - start) / 10 ** 6} ms")


if __name__ == '__main__':
    solve(ex1)
    solve(ex2)
    solve(ex3)
    solve(ex4)
    solve(ex5)
    solve(ex6)
    solve(ex7)
