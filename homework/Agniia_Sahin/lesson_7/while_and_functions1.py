number = 10

while True:
    user_input = int(input("Guess number: "))
    if user_input == number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
      
