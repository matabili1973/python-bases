with open('exer3.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

workers = {x.split()[0] : int(x.split()[1].strip('\n')) for x in lines}
print('Эти сотрудники получают жалование менее 20000:', *[(x, y) for x, y in workers.items() if y < 20000], sep = '\n')
print('Среднее жалование сотрудников:', round(sum(workers.values()) / len(workers), 2))
