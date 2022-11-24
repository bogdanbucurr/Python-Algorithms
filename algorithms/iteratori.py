class CevaClasa:

    def __init__(self):
        self.index = -1
        self.number = 0

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index > 10:
            raise StopIteration
        return self.index


generator_numere = CevaClasa()
the_iterator = iter(generator_numere)
for value in the_iterator:
    print(value)

# a_list = [1, 2, 2, 3, 4, 5, 6]
#
# the_iterator = iter(a_list)
# print(next(the_iterator))
# print(next(the_iterator))