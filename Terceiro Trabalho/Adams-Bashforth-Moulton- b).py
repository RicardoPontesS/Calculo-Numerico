import math
def calculaMetodoExplicitoF6(y5, f5, f4, f3, f2, f1, f0):
    y6 = y5 + ((0.2/720)*(2138.5*f5 - 3961.5*f4 + 4991*f3 - 3649*f2 + 1438.5*f1 - 237.5*f0))
    return y6

def calculaMetodoImplicitoF6(y5, f6, f5, f4, f3, f2,f1):
    y6I = y5 + ((0.2/720)*(237.5*f6 + 713.5*f5 - 399*f4 +241*f3 -  86.5*f2+13.5*f1))
    return y6I

def calculaf4(x4, y4):
    f4 = y4 + math.cos(x4)
    return f4

def calculaf5(x5, y5):
    f5 = y5 + math.cos(x5)
    return f5

def calculaf6(x6, y6):
    f6 = y6 + math.cos(x6)
    return f6


def calculaCriteriodeParadaY6(y6I, y6):
    erro = (y6I - y6)/y6I
    return erro

def main():
    y3 = 2.6022663747838664
    f3 = 2.8926
    f2 = 2.4213
    f1 = 2.42132
    f0 = 2
    x4 = 0.8
    x5 = 1
    x6 = 1.2
    y4 = 3.3477453190895017
    f4 = calculaf4(x4, y4)
    y5 = 4.226685306996628
    f5 = calculaf5(x5, y5)


    y6 = calculaMetodoExplicitoF6(y5,f5, f4, f3, f2, f1, f0)
    f6 = calculaf6(x6, y6)
    y6I = calculaMetodoImplicitoF6(y5, f6, f5, f4, f3, f2, f1)
    erroY6 = calculaCriteriodeParadaY6(y6I, y6)

    while erroY6 > 0.0001:
        f6 = calculaf6(x6, y6)
        y6I = calculaMetodoImplicitoF6(y5, f6, f5, f4, f3, f2, f1)
        erroY6 = calculaCriteriodeParadaY6(y6I, y6)
        y6 = y6I
    print("X6 = ", x6)
    print("Y6 = ", y6)


if __name__ == "__main__":
    main()
