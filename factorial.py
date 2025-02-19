def factorial(input=6):
    if input < 0:
        raise ValueError('You must enter a non-negative integer')
    factorial = 1
    for i in range(2, input + 1):
        print(i, factorial)
        factorial *= i
    return factorial

factorial ()