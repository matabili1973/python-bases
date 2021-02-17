with open('exer2.txt', 'r', encoding = 'utf-8') as my_file:
    lines = my_file.readlines()
    print('Количество строк в файле:', len(lines))
    for index in range(len(lines)):
        print('Строка:', index + 1, 'всего слов:', len(lines[index].split()))
