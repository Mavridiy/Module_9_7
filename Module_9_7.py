
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print("Составное")
            return result
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Пример:
result = sum_three(2, 3, 6)
print(result)
result = sum_three(5, 4, 7)
print(result)