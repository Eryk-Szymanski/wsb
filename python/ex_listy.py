'''
Dodaj listę o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Uzytkownikowi wyświetl listę do wyboru:
1) Wyświetl pierwsze 3 elementy listy
2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
3) Wyświetl zawartość listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)
Użytkownik raz dokonuje wyboru z listy.
Wyświetl zawartość listy po wykonaniu operacji przez użytkownika.
'''

while True:
    country = ['Poland', 'Germany', 'USA', 'Australia', 'UK']
    elementOne = input('Podaj pierwsze państwo: ')
    elementTwo = input('Podaj drugie państwo: ')
    country.append(elementOne)
    country.append(elementTwo)
    print('Opcje:')
    print('1) Wyświetl pierwsze 3 elementy listy')
    print('2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)')
    print('3) Wyświetl zawartość listy')
    print('4) Wyczyść zawartość listy')
    print('5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)')
    choice = input('Twój wybór: ')

    match choice:
        case '1':
            print('Trzy pierwsze elementy: ' + str(country[0:3]))
        case '2':
            print('Dodane elementy: ' + str(country[-2:]))
        case '3':
            print('Zawartość listy: ' + str(country))
        case '4':
            country.clear()
            print('Wyczyszczono listę. country: ' + str(country))
        case '5':
            find = input('Podaj szukany element: ')
            if find in country:
                print('Znaleziono podany element na miejscu ' + str(country.index(find)))
            else:
                print('Podanego elementu nie ma w liście')
        case _:
            break

    print(country)