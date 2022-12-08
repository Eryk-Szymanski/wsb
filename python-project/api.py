import requests as r
import json
from colors import Colors as c

class Api:

    # Szukanie krypto
    def cryptoSearch(self, query) -> list[list[str]]:

        try:
            params = {'query': query}
            result = r.get(url = "https://api.coingecko.com/api/v3/search", params = params)
            content = json.loads(result.content)
            
            if not 'coins' in content:
                raise Exception
            elif content['coins'] == []:
                raise Exception
            else:
                table = []
                for coin in content['coins']:
                    row = [coin['name'], coin['symbol'], coin['api_symbol']]
                    table.append(row)

                return table

        except Exception:
            print(c.FAIL + f"Niestety, nie udało się znaleźć wyników dla {query}" + c.ENDC)

    # Szukanie ceny
    def getPrice(self, query) -> None:
        import requests as r
        import json

        try:
            # Najpierw szuka krypto po podanej nazwie
            cryptos = self.cryptoSearch(query)
            cryptoName = cryptos[0][0]

            # Pobiera z wyniku id krypto -> api działa najlepiej przy z id
            cryptoId = cryptos[0][2]

            # Pobranie ceny
            params = {'ids': cryptoId, 'vs_currencies': 'pln'}
            result = r.get(url = "https://api.coingecko.com/api/v3/simple/price", params = params)
            content = json.loads(result.content)

            if content == {}:
                raise Exception
            else:
                print(f"Cena {cryptoName}: {content[cryptoId]['pln']} zł")

        except Exception:
            print(c.FAIL + f"Niestety, nie udało się pobrać ceny dla {cryptoId}" + c.ENDC)

