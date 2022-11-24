def generator_function(n):
    """
    genereaza toate numerele de la n la 0
    """
    while n != 0:
        yield n
        n -= 1
    yield n


for value in generator_function(7):
    print(value)