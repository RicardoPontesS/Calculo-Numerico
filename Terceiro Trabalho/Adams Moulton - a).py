def calculaMetodoExplicitoF4(y3,f3,f2,f1,f0):
    y4 = y3 + ((0.2/24)*(55*f3 - 59*f2 + 37*f1 - 9*f0))
    return y4

def calculaMetodoExplicitoF5(y3,f4,f3,f2,f1):
    y5 = y3 + ((0.2/24)*(55*f4 - 59*f3 + 37*f2 - 9*f1))
    return y5


def calculaf4(x4,y4):
    f4 = 2 * x4 - 3* y4 + 1
    return f4

def calculaf5(x5,y5):
    f5 = 2 * x5 - 3* y5 + 1
    return f5
def calculaMetodoImplicitoF4(y3,f4,f3,f2,f1):
    y4I = y3 + ((0.2/24)*(9*f4 + 19*f3 - 5*f2 + f1))
    return y4I

def calculaMetodoImplicitoF5(y3,f5,f4,f3,f2):
    y5I = y3 + ((0.2/24)*(9*f5 + 19*f4 - 5*f3 + f2))
    return y5I

def calculaCriteriodeParadaY4(y4I, y4):
    erro = (y4I - y4)/y4I
    return erro

def calculaCriteriodeParadaY5(y5I, y5):
    erro = (y5I - y5)/y5I
    return erro

def main():
    y3 = 0.6542
    f3 = 0.2374
    f2 = -0.1224
    f1 = -0.784
    f0 = -2
    x4 = 0.8
    x5 = 1

    y4 = calculaMetodoExplicitoF4(y3, f3, f2, f1, f0)
    f4 = calculaf4(x4, y4)
    y4I = calculaMetodoImplicitoF4(y3, f4, f3, f2, f1)
    erroY4 = calculaCriteriodeParadaY4(y4I, y4)

    while erroY4 > 0.0001:
        f4 = calculaf4(x4, y4)
        y4I = calculaMetodoImplicitoF4(y3, f4, f3, f2, f1)
        erroY4 = calculaCriteriodeParadaY4(y4I, y4)
        y4 = y4I
    print("X4 = ",x4)
    print("Y4 = ",y4)
    y5 = calculaMetodoExplicitoF5(y3, f4, f3, f2, f1)
    f5 = calculaf5(x5, y5)
    y5I = calculaMetodoImplicitoF5(y3, f5, f4, f3, f2)
    erroY5 = calculaCriteriodeParadaY5(y5I, y5)

    while erroY5 > 0.0001:
        f5 = calculaf5(x5, y5)
        y5I = calculaMetodoImplicitoF5(y3, f5, f4, f3, f2)
        erroY5 = calculaCriteriodeParadaY5(y5I, y5)
        y5 = y5I
    print("X5 = ",x5)
    print("Y5 = ",y5)
if __name__ == "__main__":
    main()
