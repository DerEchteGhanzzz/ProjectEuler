import functools as ft
import math

def get_exercise_number():
    return 5


def solve():
    nums = [i + 1 for i in range(0, 20)]
    return ft.reduce(lambda x, y: math.lcm(x, y), nums, 1)
