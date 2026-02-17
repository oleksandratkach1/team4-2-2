import utils
def is_power_of_five(n):
    """Повертає True, якщо число є степенем п'ятірки."""
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1
print(utils.factorial(8))

