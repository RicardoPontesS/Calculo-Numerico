import numpy as np
import math

def calcula_k1(x, y):
    k1 = 0.2 * (y + math.cos(x))
    return k1

def calcula_k2(x, y):
    k1 = calcula_k1(x, y)
    k2 = 0.2 * ((y + k1/2) + math.cos(x+0.2/2))
    return k2

def calcula_k3(x, y):
    k2 = calcula_k2(x, y)
    k3 = 0.2 * ((y+3/4*k2)+(math.cos(x+3/4*0.2)))
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
    tolerancia = 0.0001
    erro = float('inf')
    valores_rk = []
    iteracoes = 0

    while erro > tolerancia:
        rk = rungeKutta(x, y)
        erro = np.abs(rk - y)
        y = rk
        valores_rk.append(rk)
        iteracoes += 1

    print("Resultado final:", rk)
    print("Número de iterações:", iteracoes)
    print("Valores de Y ao longo da iteração:", valores_rk)

if __name__ == "__main__":
    main()
