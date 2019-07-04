letter = input("Enter a massage on english: ")

while True:  # key verification
    try:
        key = int(input("Enter a key:"))
        if -25 <= key <= 25:
            break
        else:
            print("Unavailable key")
            continue
    except ValueError:
        print("Key should be integer:")

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

cipher = ""
for i in letter:
    if i in alphabet:
        cipher += alphabet[(alphabet.index(i) + key * 2) % len(alphabet)]
    else:
        cipher += i  # if the symbol not in dictionary, then write it without changes

print(cipher)
