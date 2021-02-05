first, last = float(input()), float(input())
days = 1

while first < last:
    first = first * 1.1
    days += 1

print(days)
