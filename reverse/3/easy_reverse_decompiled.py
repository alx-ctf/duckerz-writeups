# uncompyle6 version 3.9.3
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.12.1 (main, Jul 10 2025, 11:57:50) [GCC 13.3.0]
# Embedded file name: easy_reverse.py
# Compiled at: 2025-02-03 10:51:52
# Size of source mod 2**32: 990 bytes
import string

def rot13(text):
    result = []
    for i in text:
        char = i - 13
        if char < 32:
            char += 95
        result.append(chr(char))
    else:
        return "".join(result)


def atbash(text):
    alphabet = string.ascii_uppercase + string.ascii_lowercase
    reversed_alphabet = alphabet[None[None:-1]]
    table = str.maketrans(alphabet + string.digits + string.punctuation, reversed_alphabet + string.digits[None[None:-1]] + string.punctuation[None[None:-1]])
    return text.translate(table)


def to_hex(text):
    result = []
    for i in text:
        result.append(hex(ord(i)))
    else:
        return result


def xor(text):
    result = []
    for i in text:
        result.append(int(i, 16) ^ 8)
    else:
        return result


def reverse_text(text):
    return text[None[None:-1]]


def to_binary(text):
    result = []
    for i in text:
        result.append(bin(ord(i))[2[:None]].zfill(8))
    else:
        return " ".join(result)


text = input()
print(to_binary(atbash(reverse_text(rot13(xor(to_hex(text)))))))

# okay decompiling __pycache__/easy_reverse.cpython-38.pyc
