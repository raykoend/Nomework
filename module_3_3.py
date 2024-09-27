def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('1.Функци с параметрами по умолчанию:')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print()


print('2.Распаковка параметров')
values_list = ('Moscow', 27, True)
print_params(*values_list)
values_dict = {'a': 12, 'b': False, 'c': 'Russia'}
print_params(**values_dict)
print()

print('3.Распаковка + отдельные параметры')
values_list2 = [52.32, 'Строка']
print(*values_list2, 42)
