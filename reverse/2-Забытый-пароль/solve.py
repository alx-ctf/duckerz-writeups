flag = b'\x1c-\x1b#\x1d*2S(\x0c\n\nO\x08J<7\x1bJ\x0c\x1bC=\x1c7/\t\x0f@7\x1b\x0c\x1d\r\x0cJU'
for key in range(256): # перебор ключей
    bytesarray = []
    for byte in flag: # декодируем каждый байт из флага
        bytesarray.append(chr(byte + key)) # добавляем 
    result = ''.join(bytesarray) # добавляем дешифрованные байты в строку
    
    # проверяем чтобы каждый элемент итоговой строки
    # был "читаемым" символом
    if all(32 <= ord(c) <= 126 for c in result):
        print(f"[+] Key: {key} -> {result}")