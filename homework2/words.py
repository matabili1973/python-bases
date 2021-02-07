word_list = list(input('Введите строку, состоящую из нескольких слов, разделенных пробелами:\n').split())

for index, value in enumerate(word_list):
    print(index+1, value[:10])
