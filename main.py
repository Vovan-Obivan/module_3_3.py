def print_params (a = 1, b = "строка", c = True):
    print(a, b, c)



values_list = [32.41, 'string', False]
values_dict = {'a': 1, 'b': 'string', 'c': True}
value_list2 = [54.32, 'Строка']



print_params()
print_params(b = 25)
print_params(c = [1, 2 ,3])
print_params(*values_list)
print_params(**values_dict)
print_params(value_list2)
print_params(*value_list2, 42)

