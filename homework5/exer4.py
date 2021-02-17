from translate import Translator

with open ('exer4.txt', 'r', encoding = 'utf-8') as f:
    lines = [x.strip('\n') for x in f.readlines()]

result = []
my_trans = Translator(from_lang = 'english', to_lang = 'russian')
for counter in range(len(lines)):
    result.append(my_trans.translate(lines[counter][:-4]) + lines[counter][-4:])

with open('exer4_2.txt', 'a', encoding = 'utf-8') as f2:
    for string in result:
        f2.write(string + '\n')
