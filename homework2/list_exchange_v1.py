my_list = list(input('Введите, пожалуйста, список значений через пробел:\n').split())


for counter in range(1, len(my_list), 2):
    my_list[counter-1], my_list[counter] = my_list[counter], my_list[counter-1]
print(my_list)
