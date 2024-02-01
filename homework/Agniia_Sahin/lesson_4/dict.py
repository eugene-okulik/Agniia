my_dict = { 
    'tuple': (1, 2, 3, None, 'text'), 
    'list': [1, 4, 'text2', False, 2.56],
    'dict': {'one' : 'value', 'two' : False, 'three' : (1, 2, 3), 'four' : 5, 'five' : True},
    'set' : {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
    }
print(my_dict['tuple'][-1]) # выведите на экран последний элемент
my_dict['list'].append(67) # добавьте в конец списка еще один элемент
poped = my_dict['list'].pop(1) # удалите второй элемент списка
print(my_dict['list'])
print(poped) # показать удаленный элемент
my_dict['dict'][('i am a tuple', )] = 'hi' # добавьте элемент с ключом ('i am a tuple',) и любым значением
del my_dict['dict']['one'] # удалите какой-нибудь элемент
print(my_dict['dict'])
my_dict['set'].add(90) # добавьте новый элемент в множество
my_dict['set'].remove('text') # удалите элемент из множества
print(my_dict['set'])
print(my_dict) # В конце выведите на экран весь словарь
