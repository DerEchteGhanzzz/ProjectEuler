def get_exercise_number():
    return 4


def is_palindromic(n):
    str_n = str(n)
    begin = 0
    end = len(str_n) - 1
    while begin < end:
        if str_n[begin] != str_n[end]:
            return False
        begin += 1
        end -= 1
    return True


def solve():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palindromic(i * j) and i * j > largest:
                largest = i * j
    return largest
