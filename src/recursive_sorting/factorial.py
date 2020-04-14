def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


print(factorial(4))

# n! = n * (n-1)!


def factorial_recursion(n):
    print(n)
    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


print(factorial_recursion(4))
