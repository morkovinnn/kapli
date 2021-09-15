y = int(input("Введите число - "))
def kapli(x):
    if x % 3 == 0:
        return "Pling"
    elif x % 5 == 0:
        return "Plang"
    elif x % 7 == 0:
        return "Plong"
    else:
        return x

print (kapli(y))