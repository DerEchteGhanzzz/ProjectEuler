def get_exercise_number():
    return 6

def gauss(n):
    return (n * (n + 1)) // 2

def solve(n=100):
    return abs(gauss(n)**2 - sum(i*i for i in range(1, n+1)))