def show():
    print('Witaj ', end='')
    print('Eryk')

show()

def iloraz(a, b):
    # return a/b
    return a//b # -> zwraca liczbę całkowitą

print(iloraz(4, 3))
print(iloraz(11, 2))

'''
Uzytkownik podaje z klawiatury markę, model, pojemność, prędkość maksymalną
Zdefiniuj funkcję, która pobierze dane od użytkownika i przypisze do słownika

Utwórz drugą funkcję wyświetlającą dane w formacie:
Marka i model: ... ...
Pojemność ...
Prędkość maksymalna: ...
'''

car = {}

def getCar():
    car['make'] = input('Podaj markę: ')
    car['model'] = input('Podaj model: ')
    car['tank'] = input('Podaj pojemność: ')
    car['max_speed'] = input('Podaj prędkość maksymalną: ')

def showCar():
    print(f'Marka i model: {car["make"]} {car["model"]}')
    print(f'Pojemność {car["tank"]}')
    print(f'Prędkość maksymalna: {car["max_speed"]}')

getCar()
showCar()