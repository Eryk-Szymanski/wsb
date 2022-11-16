slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}

print(slownik)
print(slownik['klucz1'])

'''
Utwórz słownik, o nazwie worker zawierający klucz: imie, nazwisko, miasto, wiek, imiona_dzieci, imiona_rodzicow
'''

worker = {
    'imie': 'Dariusz',
    'nazwisko': 'Mariusz',
    'miasto': 'Poznań',
    'wiek': 123,
    'imiona_dzieci': ['Helena', 'Dawid'],
    'imiona_rodzicow': ['Bogumiła', 'Zbigniew']
}

print(worker)
print(worker['imiona_rodzicow'])
print(worker['imiona_rodzicow'][0])

worker['wzrost'] = 180
print(worker)
print(worker.values())
print(worker.items())

for value in worker.values():
    print(value, end=" ")

for key, value in worker.items():
    print(f'{key}:{value}')

key = 'imie'

if key in worker:

    del worker[key]
    print(f'Klucz {key} został usunięty!')

else:

    print(f'Klucz {key} nie został usunięty!')

print(worker)

# dokończyć słowniki

slownik = {
    1: None,
    2: 20
}
