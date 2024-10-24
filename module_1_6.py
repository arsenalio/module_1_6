my_dict = {'Banana': 500, 'Potato': 300, 'Lemon': 200}
print(my_dict)
print(my_dict.get('Banana'))
print(my_dict.get('Tomato'))
my_dict.update({'Carrot': 250, 'Cucumber': 330})
print(my_dict)
a = my_dict.pop('Lemon')
print(my_dict)
print(a)
my_set = {(7,8,1.5), 7,8,9,62.456, 'Lion'}
print(my_set)
my_set.update({22, 'Eagle'})
print(my_set)
my_set.remove(8)
print(my_set)


