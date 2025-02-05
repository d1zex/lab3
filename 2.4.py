def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [10, 15, 3, 7, 2, 11, 4, 13, 18, 19]
prime_numbers = filter_prime(numbers)
print(prime_numbers)