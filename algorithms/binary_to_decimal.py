binary = input('binary = ')
d = 0
for power_of_2, digit in enumerate(binary[::-1]):
    d = d + int(digit) * 2 ** power_of_2
print(d)
