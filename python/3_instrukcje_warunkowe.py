x = input("Podaj wartość: ")

if x == '10':
    print('Podałeś 10')
    print('xzc')
else:
    print('Inna wartość niż 10')

print(type(x))

y = False
if y:
    print('prawda')
else:
    print('fałsz')

'''
    Użytkownik podaje wartości z trzech zmiennych x, y, z
    Wyświetl, która z tych trzech wartości jest największa
    Wykorzystaj instrukcje warunkowe
'''

x = input("Podaj x: ")
y = input("Podaj y: ")
z = input("Podaj z: ")

try:
    if int(x) > int(y) and int(x) > int(z):
        print("Największa to x: " + x)
    elif int(y) > int(z) and int(y) > int(x):
        print("Największa to y: " + y)
    else:
        print("Największa to z: " + z)
except Exception as e:
    print("Podane wartości muszą być liczbami.")
