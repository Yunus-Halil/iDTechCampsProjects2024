n = int(input("What number do you want to apply the factorial to: "))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n))


