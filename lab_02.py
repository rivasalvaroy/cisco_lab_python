def is_prime_a(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_b(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def is_prime_c(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


for i in range(1, 20):
    if is_prime_c(i + 1):
        print(i + 1, end=" ")
print()
