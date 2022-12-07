def fib(value):

    try:
        if value == 1 or value == 2:
            return 1
        else:
            return fib(value - 2) + fib(value -1)

    except RecursionError:
        print("Limit rekurencji przekroczony")

    except Exception as e:
        print(str(e))

    exit()

print(fib(6))