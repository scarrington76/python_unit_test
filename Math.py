## removed math wrapper in order to make calls easier


def add(a: int, b: int):
    '''calculates and returns a plus b'''
    return a + b

def multiply(a: int, b: int):
    '''calculates and returns a multiplied by b'''
    return a * b

def divide(a: int, b: int):
    ''' calculates a divided by b, raises ValueError on division by Zero'''
    if b == 0:
        raise ZeroDivisionError

    return a/b

def is_even(a: int):
    return a % 2 == 0

def power(a: int, b: int):
    '''calculates a to the power of b'''
    prod = 1
    for i in range(abs(b)):
        prod *= a

    return prod

def is_prime(num: int):
    '''finds out if num is a prime or not'''
    if num < 0:
        raise(ValueError())
    if num == 0:
        return False

    if num <=3:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def factorial(n: int):
    '''calculates n! = 1 * 2 * 3 * ... * n'''
    prod = n ## Changed original code from prod = 1 to prod = n to make factorial work
    for i in range(1, n):
        prod *= i

    return prod

def factors(number: int):
    '''finds and returns list of factors for number'''
    if number <= 0:
        raise ValueError('number must be geater than zero')
    if number == 1 or number == 2:
        return list(range(1, number))

    factors = [1, number]
    for factor in range(3, number):
        if number % factor == 0:
            factors.append(factor)

    return factors

