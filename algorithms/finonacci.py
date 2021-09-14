def fib_rec(n):
    """Рекурсивынй Фибоначчи."""
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
    

def fib_tbl(n):
    """Табличный Фибоначчи."""
    l = [0, 1]
    for i in range(2, n + 1):
        l.append(l[i - 1] + l[i - 2])
    return l[-1]


def fib_digt(n):
    """Получение последней цифры числа Фибоначчи."""
    l = [0, 1]
    for i in range(2, n + 1):
        l.append((l[i - 2] + l[i - 1]) % 10)
        print(l)
    return l[-1]


if __name__ == "__main__":
    for v in range(1, 10**7):
        # print(f"fib_rec({v}): {fib_rec(v)}.")
        # print(f"fib_tbl({v}): {fib_tbl(v)}.")
        print(f"fib_tbl({v}): {fib_digt(v)}.")
