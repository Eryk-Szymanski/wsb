from api import Api
from colors import Colors as c
from tabulate import tabulate

class Menu():

    def __init__(self) -> None:
        self.api = Api()

    def runMenu(self) -> None:

        # Wypisanie opcji menu
        print()
        print(c.BOLD + c.OKCYAN + "--- Menu ---" + c.ENDC)
        print(c.BOLD + c.OKCYAN + "1. " + c.ENDC + "Szukaj kryptowaluty")
        print(c.BOLD + c.OKCYAN + "2. " + c.ENDC + "Sprawdź cenę")
        print(c.BOLD + c.OKCYAN + "3. " + c.ENDC + "Wyjdź")

        # Pobranie opcji od użytkownika
        choice = input(c.BOLD + c.OKCYAN + "Wybierz opcję: " + c.ENDC)

        # Wywołanie wybranej opcji
        try:
            match int(choice):
                # Szukanie
                case 1:
                    search = input(c.BOLD + c.OKCYAN + "Podaj czego szukasz: " + c.ENDC)
                    result = self.api.cryptoSearch(search)
                    if result is not None:
                        print(tabulate(result, headers = ["Nazwa", "Symbol", "Symbol Api"]))
                # Cena
                case 2:
                    cryptoId = input(c.BOLD + c.OKCYAN + "Wprowadź nazwę kryptowaluty: " + c.ENDC)
                    self.api.getPrice(cryptoId)
                # Wyjście
                case 3:
                    exit()
                # Cokolowiek innego
                case _:
                    print(c.FAIL + "Wybierz poprawną opcję..." + c.ENDC)
        
        except Exception:
            print(c.FAIL + "Wybierz poprawną opcję..." + c.ENDC)

        # Rekurencyjne wywołanie menu
        self.runMenu()

# Początek programu
print(c.WARNING + c.BOLD + c.UNDERLINE + "Witaj w CryptoInfo!" + c.ENDC)
print(c.WARNING + "Znajdź informacje, których potrzebujesz..." + c.ENDC)

# Inicjalizajca Menu
menu = Menu()
menu.runMenu()

