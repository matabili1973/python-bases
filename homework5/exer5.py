from random import randint

with open ('exer5.txt', 'a', encoding = 'utf-8') as f:
    f.write(' '.join([str(randint(1, 1000)) for x in range(20)]) + '\n')

with open ('exer5.txt', 'r', encoding = 'utf-8') as f2:
    summ = 0
    for line in f2:
        summ += sum([int(x) for x in line.strip('\n').split()])

print(summ)
