import re

alphabet = "abcdefghijklmnopqrstuvwxyz"
bigAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter = input("Enter a massage: ")
key = input("Enter a secret word:")
cipher = ""

j = 0
for i in letter:
    if re.search(r"[A-Z]", i) or re.search(r"[a-z]", i):
        if i in alphabet:
            index = (alphabet.index(i) + alphabet.index(key[j])) % 33
            cipher += alphabet[index]
        else:
            index = (bigAlphabet.index(i) + alphabet.index(key[j])) % 33
            cipher += bigAlphabet[index]
        if j == len(key) - 1:
            j = 0
        else:
            j += 1
    else:
        cipher += i

print(cipher)
