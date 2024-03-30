import random

salary = int(input("What is your salary?"))
bonus = random.choice([True, False])
bonus_amount = random.randint(10, 100)
if bonus:
    print(f"{salary}, {bonus} - $'{salary+bonus_amount}'")
else:
    print(f"{salary}, {bonus} - $'{salary}'")

