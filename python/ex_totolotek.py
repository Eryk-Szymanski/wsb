# Utwórz program totolotek, użytkownik podaje 6 liczb

import random as r

nums = []

print('Podaj sześć liczb w zakresie od 1 do 49')
for i in range(1, 7):
    num = input(f'Podaj {i} liczbę: ')
    while True:
        if num not in nums and 1 <= int(num) <= 49:
            nums.append(num)
            break
        else:
            num = input(f'Podana liczba jest już w liście lub jest po za zakresem. Podaj inną {i} liczbę: ')

print(nums)

for index, num in enumerate(nums):
    rand = r.randrange(1, 50)
    print(num, rand)
    if num == rand:
        print(f'Liczba {index + 1} odgadnięta!')
    else:
        print(f'Liczba {index + 1} jest inna')
