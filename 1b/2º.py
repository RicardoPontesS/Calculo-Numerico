import sympy as sp
import numpy as np
def retornoFuncao(x):
    resultado = 2 * x**3 - 6 * x - 1
    return resultado


def verificaContinuidade(funcao, intervalo):
    x = sp.symbols('x')
    pontos = np.linspace(float(intervalo[0]), float(intervalo[1]), 100)

    print(
        f"Calculando os limites laterais para verificar a continuidade da função no intervalo [{intervalo[0]},{intervalo[1]}]...")

    for ponto in pontos:
        limite_esquerda = sp.limit(funcao, x, ponto, dir='-')
        limite_direita = sp.limit(funcao, x, ponto, dir='+')
        valor_ponto = funcao.subs(x, ponto)

        if limite_esquerda != limite_direita != valor_ponto:
            print(f"A função não é contínua em x = {ponto}")
            return False

    return True


def verificaDerivadaContinua(funcao, intervalo):
    x = sp.symbols('x')
    derivada = sp.diff(funcao, x)
    print(f"A derivada da G(X) é: {derivada}")

    for ponto in np.linspace(float(intervalo[0]), float(intervalo[1]), 100):
        limite_esquerda = sp.limit(derivada, x, ponto, dir='-')
        limite_direita = sp.limit(derivada, x, ponto, dir='+')
        valor_ponto = derivada.subs(x, ponto)

        if limite_esquerda != limite_direita != valor_ponto:
            print(f"A derivada não é contínua em x = {ponto}")
            return False

    return True


def verificaDerivadaMenorQueUm(derivada, intervalo):
    x = sp.symbols('x')

    for ponto in np.linspace(float(intervalo[0]), float(intervalo[1]), 100):
        valor_ponto = derivada.subs(x, ponto)
        if abs(valor_ponto)>= 1:
            print(f"Derivada é maior ou igual a 1 em x = {ponto}")
            return False

    return True


def verificaFuncoes(intervalo):
    x = sp.symbols('x')
    funcoes = modificaFuncao()

    funcao_continua = None

    for eq in funcoes:
        print(f"G(X) sendo análisada: {eq}")
        if verificaContinuidade(eq, intervalo):
            print(f"A G(X): {eq} É contínua.")
            funcao_continua = eq
            break

    if funcao_continua:
        if verificaDerivadaContinua(funcao_continua, intervalo):
            print(f"A derivada também é contínua no intervalo.")
            derivada = sp.diff(funcao_continua, x)
            if verificaDerivadaMenorQueUm(derivada, intervalo):
                print("A derivada é menor que 1 em todo o intervalo.")
                print(f"A função {funcao_continua} está apta para receber as iterações")
                return funcao_continua
            else:
                print("A função G(X) não satisfaz todos os critérios")
    else:
        print("\nNenhuma função contínua encontrada.")

    return funcao_continua


def iteracoes(funcao_continua):
    cont = 0
    convergencia = 0
    x = sp.symbols('x')
    epsilon = 0.0000001
    intervalo = verificaIntervalo()
    x0 = (intervalo[0] + intervalo[1]) / 2

    funcao = funcao_continua

    xk = funcao.subs(x, x0)
    xk_anterior = x0

    while abs(xk - xk_anterior) > epsilon:
        xk_anterior = xk
        xk = funcao.subs(x, xk_anterior)
        print(xk)
    raiz = xk
    x0 = (intervalo[0] + intervalo[1]) / 2

    funcao = funcao_continua

    xk = funcao.subs(x, x0)
    xk_anterior = x0
    while abs(xk - xk_anterior) > epsilon:
        if (cont >= 2):
            convergencia = (xk-raiz) / (xk_anterior-raiz)
            xk_anterior = xk
            xk = funcao.subs(x, xk_anterior)
        cont = cont + 1
        print(convergencia)
    print(f"Raiz encontrada: {raiz}")


def verificaIntervalo():
    retorno1 = 0
    retorno2 = 0
    comecoIntervalo = 0
    fimIntervalo = 0
    i = 1
    comecoIntervalo = retornoFuncao(i)
    fimIntervalo = retornoFuncao(i + 1)

    while not ((retorno1 > 0 and retorno2 < 0) or (retorno1 < 0 and retorno2 > 0)):
        retorno1 = retornoFuncao(i)
        retorno2 = retornoFuncao(i + 1)
        comecoIntervalo = i
        fimIntervalo = i + 1
        i = i + 1
        if i > 15:
            i = -15

    intervalo = [comecoIntervalo, fimIntervalo]
    print(f"Existe um zero no intervalo: [{comecoIntervalo},{fimIntervalo}]")
    return intervalo


def calculaEExibeDerivada(equacao, x):
    derivada = sp.diff(equacao, x)
    return derivada


def modificaFuncao():

    x = sp.symbols('x')

    equacoes_com_x_isolado = []

    # x = sqrt((6x+1)/2)
    equacao1 = ((6 * x + 1) / 2) ** (1 / 3)
    equacoes_com_x_isolado.append(equacao1)

    for eq in equacoes_com_x_isolado:
        derivada = calculaEExibeDerivada(eq, x)
    return equacoes_com_x_isolado


if __name__ == '__main__':
    intervalo = verificaIntervalo()

    funcao_continua = verificaFuncoes(intervalo)

    if funcao_continua:
        iteracoes(funcao_continua)