import string

def unrot13(text):
    result = []
    for c in text:
        code = ord(c) + 13
        if code > 126:
            code -= 95
        result.append(chr(code))
    return "".join(result)

def atbash(text):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(
        alphabet + string.digits + string.punctuation,
        reversed_alphabet + string.digits[::-1] + string.punctuation[::-1]
    )
    return text.translate(table)

def reverse_text(text):
    return text[::-1]

def un_xor(nums):
    return [n ^ 8 for n in nums]

def from_hex(nums):
    return "".join(chr(n) for n in nums)

def from_binary(bin_str):
    return "".join(chr(int(b, 2)) for b in bin_str.split())

# --- данные ---
bins = "01010011 01011011 00111101 00111001 01001110 00111101 01001010 00111101 01001110 01110001 01100010 00111111 01110001 01000000 00110111 01010000 01010111 01001110 00100111 01010101 01110110 01101110 00101011 00110011 00101101 01101011 00101100"

# --- расшифровка ---
step1 = from_binary(bins)          # → строка
step2 = atbash(step1)              # atbash обратим
step3 = reverse_text(step2)        # reverse обратим
step4 = unrot13(step3)             # раскручиваем rot13
step5 = [ord(c) for c in step4]    # символы → числа
step6 = un_xor(step5)              # XOR с 8 обратим
flag = from_hex(step6)             # числа → строка

print(flag)

