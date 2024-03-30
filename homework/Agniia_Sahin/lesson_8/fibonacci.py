def fibonacci(n):
    if type(n) != int or n < 0:
        print("invalid value")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


number_5 = fibonacci(5)
number_200 = fibonacci(200)
number_1000 = fibonacci(1000)
number_100000 = fibonacci(100000)

print(number_5)
print(number_200)
print(number_1000)
print(number_100000)

