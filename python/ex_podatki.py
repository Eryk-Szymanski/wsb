def calcTax(salary):

    match salary * 12:
        case _ if salary < 120000:
            return salary * 0.19
        case _ if salary < 240000:
            return salary * 0.15
        case _ if salary < 400000:
            return salary * 0.10
        case default:
            return salary * 0.08

payersAndSalaries = {}

def getPayers(n):
    for i in range(0, n):
        name = input("Podaj imię: ")
        salary = input("Podaj wypłatę na miesiąc: ")
        payersAndSalaries[name] = salary

def drawGraph():
    import matplotlib.pyplot as plt


getPayers(3)
drawGraph();
print(payersAndSalaries)

