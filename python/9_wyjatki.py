#try except
def div(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return 'Nie wolno dzielić przez zero'

print(div(3, 0))

# Użytkownik podaje z klawiatury wartość (liczba całkowita) do momentu podania liczby całkowitej
def func():
    while True:
        try:
            value = int(input("Podaj liczbę całkowitą: "))
            print(f"Wartość {value} jest liczbą całkowitą")
            break
        except ValueError:
            print("Podana wartośc nie jest liczbą całkowitą")

# Funkcja obliczająca pole kwadratu
class NullValueError(Exception):
    pass

def square():
    import math
    while True:
        try:
            x = float(input("Podaj długość boku kwadratu: "))
            if x <= 0:
                raise NullValueError
            print(f"Pole kwadratu wynosi {math.pow(x, 2)}")
            break

        except ValueError:
            print("Podana wartość nie jest liczbą")

        except NullValueError:
            print("Długość boku kwadratu musi być dodatnia")

        except OverflowError:
            print("Podana liczba jest zbyt duża")

        except ArithmeticError as e:
            print("Błąd: " + str(e))

        except Exception as e:
            print("Błąd: " + str(e))

square()