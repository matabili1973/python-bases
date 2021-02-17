my_dict = {}
with open ('exer6.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        my_dict[line.split()[0]] = [x for x in line.split()[1:] if '(' in x] 

for a in my_dict.keys():
    for b in range(len(my_dict[a])):
        my_dict[a][b] = int(my_dict[a][b][:(my_dict[a][b].index('('))])
    my_dict[a] = sum(my_dict[a])
print(my_dict)
