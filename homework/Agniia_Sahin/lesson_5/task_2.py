result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

index_result_1 = result_1.index('42')
number_1 = int(result_1[index_result_1:])

index_result_2 = result_2.index('514')
number_2 = int(result_2[index_result_2:])

index_result_3 = result_3.index('9')
number_3 = int(result_3[index_result_3:])

print(number_1 + 10)
print(number_2 + 10)
print(number_3 + 10)
