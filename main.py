import binascii

file_path = '/home/amirradjou/1.txt'

x = ""
with open(file_path, 'rb') as f:
    for chunk in iter(lambda: f.read(32), b''):
        x += str(binascii.hexlify(chunk)).replace("b", "").replace("'", "")
b = bin(int(x, 16)).replace('b', '')
g = [b[i:i + 2] for i in range(0, len(b), 2)]
dna = ""
print(x)  # hexdump
print(b)  # converted to binary
