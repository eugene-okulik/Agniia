import sys

sys.set_int_max_str_digits(50000)


def fibonacci():
    predposlednee = 0
    poslednee = 1
    while True:
        yield predposlednee
        old_predposlednee = predposlednee
        predposlednee = poslednee
        poslednee += old_predposlednee


count = 0
for number in fibonacci():
    count += 1
    if count == 5:
        print(number)
    elif count == 200:
        print(number)
    elif count == 1000:
        print(number)
    elif count == 100000:
        print(number)
        break
