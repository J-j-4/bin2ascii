import binascii

print('Are you converting bin to ascii? [y/n]')
h = input('> ')
if h[0] == 'y':
    print('Input binary sequence with spaces.')
    text = input('> ')
    split = text.split(' ')
    to_return = ''
    for i in split:
        n = int('0b' + i, 2)
        ascii_char = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        to_return += ascii_char
    print(to_return)
else:
    print('Input ascii sequence.')
    text = input('> ')
    to_return = ''
    for i in text:
        binary = bin(int.from_bytes(i.encode(), 'big'))
        to_return += binary[2:] + ' '
    print(to_return)
