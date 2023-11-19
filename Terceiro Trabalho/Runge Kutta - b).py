import numpy as np
import math

def calcula_k1(x, y):
    k1 = 0.2 * (y + math.cos(x))
    return k1

def calcula_k2(x, y):
    k1 = calcula_k1(x, y)
    xk2 = (x+0.2/2)
    yk2 = (y+k1/2)
    k2 = 0.2 * (yk2 + math.cos(xk2))
    return k2

def calcula_k3(x, y):
    k2 = calcula_k2(x, y)
    xk3 = (x + 3/4 * 0.2)
    yk3 = (y + 3/4 * k2)
    k3 = 0.2 * (yk3 + math.cos(xk3))
    return k3

def rungeKutta(x, y):
    k1 = calcula_k1(x, y)
    k2 = calcula_k2(x, y)
    k3 = calcula_k3(x, y)
    y_next = y + 2 / 9 * k1 + 1 / 3 * k2 + 4 / 9 * k3
    return y_next

def main():
    x = 0
    y = 1
    num_iteracoes = 3
    valores_rk = []

    for _ in range(num_iteracoes):
        rk = rungeKutta(x, y)
        x = x + 0.2
        y = rk
        valores_rk.append(rk)

    print("Resultados nas primeiras 3 iterações:", valores_rk)

if __name__ == "__main__":
    main()
