numbers = range(1, 101)

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
    elif number % 3 == 0:
        print("fuzz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
