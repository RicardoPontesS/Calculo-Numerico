import math


def calculaMetodoExplicitoF4(y3, f3, f2, f1, f0):
    y4 = y3 + ((0.2/24)*(55*f3 - 59*f2 + 37*f1 - 9*f0))
    return y4

def calculaMetodoExplicitoF5(y4, f4, f3, f2, f1):
    y5 = y4 + ((0.2/24)*(55*f4 - 59*f3 + 37*f2 - 9*f1))
    return y5

def calculaMetodoExplicitoF6(y5, f5, f4, f3, f2):
    y6 = y5 + ((0.2/24)*(55*f5 - 59*f4 + 37*f3 - 9*f2))
    return y6

def calculaf4(x4, y4):
    f4 = y4 + math.cos(x4)
    return f4

def calculaf5(x5, y5):
    f5 = y5 + math.cos(x5)
    return f5

def calculaf6(x6, y6):
    f6 = y6 + math.cos(x6)
    return f6

def calculaMetodoImplicitoF4(y3, f4, f3, f2, f1):
    y4I = y3 + ((0.2/24)*(9*f4 + 19*f3 - 5*f2 + f1))
    return y4I

def calculaMetodoImplicitoF5(y4, f5, f4, f3, f2):
    y5I = y4 + ((0.2/24)*(9*f5 + 19*f4 - 5*f3 + f2))
    return y5I

def calculaMetodoImplicitoF6(y5, f6, f5, f4, f3):
    y6I = y5 + ((0.2/24)*(9*f6 + 19*f5 - 5*f4 + f3))
    return y6I

def calculaCriteriodeParadaY4(y4I, y4):
    erro = (y4I - y4)/y4I
    return erro

def calculaCriteriodeParadaY5(y5I, y5):
    erro = (y5I - y5)/y5I
    return erro

def calculaCriteriodeParadaY6(y6I, y6):
    erro = (y6I - y6)/y6I
    return erro

def main():
    y3 = 2.6022663747838664
    f3 = 3.42759
    f2 = 2.89265
    f1 = 2.42132
    f0 = 0.54030230586
    x4 = 0.8
    x5 = 1
    x6 = 1.2

    y4 = calculaMetodoExplicitoF4(y3, f3, f2, f1, f0)
    f4 = calculaf4(x4, y4)
    y4I = calculaMetodoImplicitoF4(y3, f4, f3, f2, f1)
    erroY4 = calculaCriteriodeParadaY4(y4I, y4)

    while erroY4 > 0.0001:
        f4 = calculaf4(x4, y4)
        y4I = calculaMetodoImplicitoF4(y3, f4, f3, f2, f1)
        erroY4 = calculaCriteriodeParadaY4(y4I, y4)
        y4 = y4I
    print("X4 = ", x4)
    print("Y4 = ", y4)

    y5 = calculaMetodoExplicitoF5(y4, f4, f3, f2, f1)
    f5 = calculaf5(x5, y5)
    y5I = calculaMetodoImplicitoF5(y4, f5, f4, f3, f2)
    erroY5 = calculaCriteriodeParadaY5(y5I, y5)

    while erroY5 > 0.0001:
        f5 = calculaf5(x5, y5)
        y5I = calculaMetodoImplicitoF5(y4, f5, f4, f3, f2)
        erroY5 = calculaCriteriodeParadaY5(y5I, y5)
        y5 = y5I
    print("X5 = ", x5)
    print("Y5 = ", y5)

    y6 = calculaMetodoExplicitoF6(y5, f5, f4, f3, f2)
    f6 = calculaf6(x6, y6)
    y6I = calculaMetodoImplicitoF6(y5, f6, f5, f4, f3)
    erroY6 = calculaCriteriodeParadaY6(y6I, y6)

    while erroY6 > 0.0001:
        f6 = calculaf6(x6, y6)
        y6I = calculaMetodoImplicitoF6(y5, f6, f5, f4, f3)
        erroY6 = calculaCriteriodeParadaY6(y6I, y6)
        y6 = y6I
    print("X6 = ", x6)
    print("Y6 = ", y6)

if __name__ == "__main__":
    main()
