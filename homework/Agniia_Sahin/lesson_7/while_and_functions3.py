def process_result(result):
    return int(result[result.index(':') + 2:]) + 10


result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

number_1 = process_result(result_1)
number_2 = process_result(result_2)
number_3 = process_result(result_3)

print(number_1, number_2, number_3)
