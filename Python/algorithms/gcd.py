from random import randint


def _gcd(a, b):
    """Алгоритм Евклида для поиска наибольшего общего делителя (НОД/GCD)."""
    if a == 0 or b == 0:
        return max(a, b)
    else:
        max_v, min_v = max(a, b), min(a, b)
        return _gcd(max_v % min_v, min_v)


if __name__ == "__main__":
    a, b = randint(1, 2 * 10**7), randint(1, 2 * 10**7)
    print(_gcd(a, b))
