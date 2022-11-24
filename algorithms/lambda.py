from functools import reduce

# suma patratelor numerelor impare dintr-o lista cu valori
lista_numere = [1, 2, 3, 4]
lista_numere = filter(lambda nr: nr % 2 != 0, lista_numere)
lista_patrate = map(lambda nr: nr ** 2, lista_numere)
suma = reduce(lambda first, second: first + second, lista_patrate, 0)
print(suma)