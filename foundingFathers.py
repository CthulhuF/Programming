fathers = {
    "Bjarne Stroustrup": "C++",
    "Ken Thompson": "C",
    "Dennis Ritchie": "C",
    "Steven Richard Born": "C",
    "James Gosling": "Java",
    "Rasmus Lerdorf": "PHP",
    "Yukihiro Matsumoto": "Ruby",
    "Larry Wall": "Perl",
    "Guido van Rossum": "Python",
    "John George Kemeny": "Basic",
    "Anders Hejlsberg": "Delphi",
    "Richard Matthew Stallman": "GNU",
    "Walter Bright": "D",
    "Andrei Alexandrescu": "D",
}
#Input Validation
while True:
    try:
        opearation = int(input("What do you want to do? 1-Search for names and surnames, 2-Sort the dictionary\t"))
        if opearation == 1 or opearation == 2:
            break
        else:
            print("Enter operation correctly")
    except:
        print("Enter operation correctly")

#Finding the key
if opearation == 1:
    while True:
        search = input("Enter the name of the founder of the language:")
        if search in fathers:
            print("He founded:", fathers[search])
            break
        else:
            print("Enter the name correctly")
if opearation == 2:
    list_name = list(fathers.keys())
    for i in sorted(list_name):
        print(i, ':', fathers[i])