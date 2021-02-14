def fact(arg1):
    def factor(arg2):
        result = 1
        if arg2:
            for counter2 in range(1, arg2 + 1):
                result *= counter2
        return result
    for counter in range(1, arg1 + 1):
        yield factor(counter)

for a in fact(10):
    print(a)
