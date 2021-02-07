my_list = list(input('Введите, пожалуйста, список значений через пробел:\n').split())


for index, value in enumerate(my_list):
    if index % 2:
        my_list[index-1], my_list[index] = my_list[index], my_list[index-1]
print(my_list)
