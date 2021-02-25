class Matrix:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __add__(self, other):
        new_list = []
        for counter in range(len(self.list_of_lists)):
            new_list.append([])
            for elements, elements2 in zip(self.list_of_lists[counter], other.list_of_lists[counter]):
                new_list[-1].append(elements + elements2)
        return Matrix(new_list)

    def __str__(self):
        new_string = ''
        for line in self.list_of_lists:
            new_string += (' '.join([str(x) for x in line]) + '\n')
        return new_string

a = Matrix([[-1, 14, 5, 9], [2, 28, -3, 0], [6, 1, -13, 5.9], [3, 7, 1, 8]])
b = Matrix([[5, 8, -2, 11], [6, -9, 24, 9], [0, -4, 8.3, 4], [-5, 10, 115, -89]])

print(a + b)
