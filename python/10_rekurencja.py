def potega(podstawa, wykladnik):
    if wykladnik == 0:
        return 1
    else: 
        return podstawa * potega(podstawa, wykladnik - 1)

print(potega(3, 3))