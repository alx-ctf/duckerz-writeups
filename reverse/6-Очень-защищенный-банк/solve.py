s = "erpgmop5pmp+fA343v5345MPVrevpmMVi44voPMI"
result = [0] * 41
for i in range(len(s)):
    c = ord(s[i])

    if (i & 1) == 0:
        c &= 0x19
        c ^= 0x22
        c |= 2

    if i % 3 == 0:
        c &= 3
        c ^= 7
        c |= 0x45

    if (i & 3) == 0:
        c += 4
        c += 4  # то же, что c += 8
        c |= 3

    if i % 5 == 0:
        c ^= 4
        c |= 6

#-----------------------------------------------
    if i == 6:
        c ^= 0x10
        c |= 0x20
    elif i == 7:
        c ^= 5
        c &= ~0x80 & 0xFF  # важно: работаем с 8 битами
    elif i == 8:
        c = (c + 1) & 0xFF
        c ^= 3
    elif i == 9:
        c |= 2
        c ^= 1
    elif i == 10:
        c &= ~0x80 & 0xFF
        c ^= 8
    elif i == 11:
        c |= 4
        c ^= 2
    elif i == 12:
        c ^= 6
        c |= 0x10
    elif i == 13:
        c &= 0x5B
        c ^= 7
    elif i == 15:
        c ^= 4
        c &= 0x6B
    elif i == 16:
        c |= 8
        c ^= 5
    elif i == 17:
        c ^= 7
        c &= 0x7E
    elif i == 18:
        c += 3
        c ^= 2
    elif i == 19:
        c |= 1
        c ^= 6
    elif i == 20:
        c ^= 3
        c &= ~0x80 & 0xFF
    elif i == 21:
        c |= 5
        c ^= 4
    elif i == 22:
        c += 1
        c ^= 3
    elif i == 23:
        c &= 0x6F
        c ^= 2
    elif i == 24:
        c |= 8
        c ^= 1
    elif i == 25:
        c ^= 7
        c &= 0x7B
    elif i == 26:
        c += 4
        c ^= 6
    elif i == 27:
        c |= 2
        c ^= 3
    elif i == 28:
        c ^= 1
        c &= 0x7E
    elif i == 29:
        c |= 4
        c ^= 6
    elif i == 30:
        c += 1
        c ^= 3
    elif i == 31:
        c &= 0x6F
        c ^= 2
    elif i == 32:
        c |= 8
        c ^= 1
    elif i == 33:
        c ^= 7
        c &= 0x7F
    elif i == 34:
        c += 2
        c ^= 4
    elif i == 35:
        c |= 3
        c ^= 5
    elif i == 36:
        c ^= 6
        c &= 0x7E

    result[i] = c & 0xFF  # убедимся что в пределах байта
# Преобразуем в строку
flag = ''.join(chr(b) for b in result if b != 0)
print("DUCKERZ{" + flag + "}")