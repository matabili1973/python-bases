import json
my_dict = {}
with open('exer7.txt', 'r') as f:
    for line in f:
        my_dict[line.split()[0]] = int(line.split()[2]) - int(line.split()[3])

firms, total_income = 0, 0
for counter in my_dict.values():
    if counter >= 0:
        firms += 1
        total_income += counter

my_json = [
    my_dict,
    {'average_profit': total_income / firms}
    ]

with open('exer7.json', 'w') as jsf:
    json.dump(my_json, jsf)
