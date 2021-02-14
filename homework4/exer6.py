from itertools import count, cycle

for number in count(3):
    print(number)
    if number == 10:
        break

my_counter = 0
for number in cycle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
    print(number)
    my_counter += 1
    if my_counter >= 50:
        break
