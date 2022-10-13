print("test")
print(2)

x = 10.1264
print(x)
print("{:.2f}".format(x))

# potegowanie
pow = 2 ** 10
print(pow)

# pobieranie danych z klawiatury

print("text")

# XOR
x = 6
y = 6
result=x^y
print(result)

# konkatynacja +
name=input()
print("Twoje imię: " + name)

length = len(name)
print(length)
print()
firstLetter = name[0]
print(firstLetter)
print(type(name))
print(type(x))
input("\nPodaj swój wiek: ")
lastLetter = name[-1]
print(lastLetter)

# konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))
x = x / 2
print(x)
print(type(x))

surname = "Kowalski"
print(surname[0]) # K
print(surname[0:3]) # Kow
print(surname[-2]) # k
print(surname[-2:]) # ki
print(surname[:-2]) # Kowals
print(surname[:-2:2]) # Kwl
