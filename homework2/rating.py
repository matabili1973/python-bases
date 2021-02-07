rating = [9, 9, 7, 5, 5, 4, 2, 1]
number = int(input('Введите целое число:\n'))

for counter in range(1, len(rating)):
    if number > max(rating):
        rating.insert(0, number)
    elif rating[counter] < number and rating[counter-1] >= number:
        rating.insert(counter, number)
        break

print(rating)
