def my_summ(a):
    global flag
    my_list = []
    if 'q' not in a:
        my_list = [int(x) for x in a]
    else:
        for counter in a:
            if counter != 'q':
                my_list.append(int(counter))
            else:
                flag = 'q'
                break
    return sum(my_list)

flag = ''
result = 0
while flag != 'q':
    my_string = input('Введите строку числе, разделенных пробелами:\n').split()
    result += my_summ(my_string)
    print(result)
