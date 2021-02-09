def int_func(a):
    return a.capitalize()

my_string = [x for x in input('Введите строку со словами, разделенными пробелом:\n').split()]
for counter in range(len(my_string)):
    my_string[counter] = int_func(my_string[counter])

print(' '.join(my_string))
