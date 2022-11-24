d = int(input('d = '))
binary = ''
while d != 0:
    r = d % 2
    binary = str(r) + binary
    d = d // 2
print(binary)
