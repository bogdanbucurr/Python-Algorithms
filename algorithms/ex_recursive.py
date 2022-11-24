'''

Sa se calculeze recursiv suma numerelor de la 0 pana la un parametru n

'''

def suma(n):
    if n == 0:
        return 0
    else:
        return n+suma(n-1)

print(suma(5))
