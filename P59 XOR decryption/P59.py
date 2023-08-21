import string
import itertools

def asciiToText(text):
    return "".join(chr(i) for i in text)

def P59(text):
    letters = [ord(c) for c in list(string.ascii_lowercase)]
    text = list(map(int, text.split(",")))
    for key in itertools.permutations(letters, 3):
        c = 0
        new_text = []
        for t in text:
            new_text.append(key[c%3] ^ t)
            c += 1
        string_t = asciiToText(new_text)
        if "that" in string_t:
            print(string_t)
            print(key)
            print(sum(new_text))
    return 0

with open("p059_cipher.txt") as f:
    text = f.read()

print(P59(text))