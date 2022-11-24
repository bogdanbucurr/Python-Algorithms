def decimal_to_binary(d):
    binary = ''
    while d != 0:
        r = d % 2
        binary = str(r) + binary
        d = d // 2
    return binary

def binary_to_decimal(binary):
    d = 0
    for power_of_2, digit in enumerate(binary[::-1]):
        d = d + int(digit) * 2 ** power_of_2
    return d

if __name__ == '__main__':
    bin = decimal_to_binary(7)
    dec = binary_to_decimal(bin)
    assert dec==7