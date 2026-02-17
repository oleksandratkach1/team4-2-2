def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def is_prime(n):
    """Повертає True, якщо число просте, інакше False."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """Повертає n-те число Фібоначчі (нумерація з 0)."""
    if n < 0:
        raise ValueError("n має бути невід'ємним")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
