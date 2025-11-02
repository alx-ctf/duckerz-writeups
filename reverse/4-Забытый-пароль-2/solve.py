message = b"t-q*u*h\x1a@L\x00SGH`\x05o;`US\x13\x01%o\x0f\x03\x15X'jQB\x05"
key = "0x2a"
list_output = []
for i in range(0, len(message)):
    a = (message[i])
    b = ord(key[i % len(key)])
    c = chr(a ^ b)
    list_output.append(c)
str_ouput = ''.join(list_output)
print(str_ouput.encode())