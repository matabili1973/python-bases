with open('my_text.txt', 'a', encoding = 'utf-8') as my_file:
    while True:
        my_line = input('Введите строку для записи, либо пустую строку для окончания\n')
        if my_line == '':
            break
        my_file.write(my_line + '\n')
