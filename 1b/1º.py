import sympy as sp
import numpy as np

def retornoFuncao(x):
    resultado = 2 * x**3 - 6 * x - 1
    return resultado

def retornoFuncao2(x):
    resultado = (2 * x**3 - 1)/6
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

def verificaDerivadaContinua(funcao, intervalos):
    x = sp.symbols('x')
    derivada = sp.diff(funcao, x)
    print(f"A derivada da G(X) é: {derivada}")

    for intervalo in intervalos:
        print(f"Calculando a continuidade da derivada para o intervalo: [{intervalo[0]},{intervalo[1]}]...")
        for ponto in np.linspace(float(intervalo[0]), float(intervalo[1]), 100):
            limite_esquerda = sp.limit(derivada, x, ponto, dir='-')
            limite_direita = sp.limit(derivada, x, ponto, dir='+')
            valor_ponto = derivada.subs(x, ponto)

            if limite_esquerda != limite_direita != valor_ponto:
                print(f"A derivada não é contínua em x = {ponto} no intervalo {intervalo}")
                return False

    return True


def verificaDerivadaMenorQueUm(derivada, intervalos):
    x = sp.symbols('x')

    for intervalo in intervalos:
        print(f"Calculando se há um número maior ou igual a 1 na derivada para o intervalo: [{intervalo[0]},{intervalo[1]}]...")
        for ponto in np.linspace(intervalo[0], intervalo[1], 100):
            valor_ponto = derivada.subs(x, ponto)
            if abs(valor_ponto) >= 1:
                print(f"Derivada é maior ou igual a 1 em x = {ponto} no intervalo {intervalo}...")

    print("-------------------------------------------------------------")
    return True

def verificaFuncoes(intervalos):
    x = sp.symbols('x')
    funcoes = modificaFuncao()

    funcao_continua = None

    for eq in funcoes:
        print(f"G(X) sendo análisada: {eq}")
        for intervalo in intervalos:
            if verificaContinuidade(eq, intervalo):
                print(f"A G(X): {eq} É contínua no intervalo [{intervalo[0]}, {intervalo[1]}].")
                funcao_continua = eq
    print("------------------------------------------------------------------------------------")

    if funcao_continua:
        if verificaDerivadaContinua(funcao_continua, intervalos):  # Verifique a derivada no primeiro intervalo
            print(f"A derivada também é contínua para todos os intervalo.")
            print("------------------------------------------------------------------------------------")
            derivada = sp.diff(funcao_continua, x)
            verificaDerivadaMenorQueUm(derivada, intervalos)
            return funcao_continua
    else:
        print("\nNenhuma função contínua encontrada.")

    return funcao_continua


def iteracoes(funcao_continua, intervalos):
    cont = 0
    convergencia = 0
    x = sp.symbols('x')
    epsilon = 0.0000001

    for intervalo in intervalos:
        x0 = (intervalo[0] + intervalo[1]) / 2  # Ponto médio do intervalo
        funcao = funcao_continua
        xk = retornoFuncao2(x0)
        xk_anterior = x0

        while abs(xk - xk_anterior) > epsilon:
            xk_anterior = xk
            xk = retornoFuncao2(xk_anterior)
        raiz = xk

        funcao = funcao_continua
        xk = retornoFuncao2(x0)
        xk_anterior = x0
        while abs(xk - xk_anterior) > epsilon:
            if (cont >= 2):
                convergencia = (xk - raiz) / (xk_anterior - raiz)
                xk_anterior = xk
                xk = retornoFuncao2(xk_anterior)
            cont = cont + 1
            #print(convergencia)
        print(f"Raiz encontrada no intervalo [{intervalo[0]}, {intervalo[1]}]: {raiz}")


def verificaIntervalo():
    retorno1 = 0
    retorno2 = 0
    comecoIntervalo = 0
    fimIntervalo = 0
    intervalos = []  # Lista para armazenar os intervalos satisfatórios
    i = -15
    comecoIntervalo = retornoFuncao(i)
    fimIntervalo = retornoFuncao(i + 1)

    while i < 15:  # Defina o limite superior adequado para a busca de intervalos
        retorno1 = retornoFuncao(i)
        retorno2 = retornoFuncao(i + 1)

        if (retorno1 > 0 and retorno2 < 0) or (retorno1 < 0 and retorno2 > 0):
            comecoIntervalo = i
            fimIntervalo = i + 1
            intervalos.append([comecoIntervalo, fimIntervalo])

        i += 1
    print("------------------------------------------------------------------------------------")
    print("Intervalos onde existe um zero na f(x):")
    for intervalo in intervalos:
        print(f"[{intervalo[0]}, {intervalo[1]}]")
    print("------------------------------------------------------------------------------------")
    return intervalos


def calculaEExibeDerivada(equacao, x):
    derivada = sp.diff(equacao, x)
    return derivada


def modificaFuncao():

    x = sp.symbols('x')

    equacoes_com_x_isolado = []
    equacao1 = (2 * x ** 3 - 1) / 6
    equacoes_com_x_isolado.append(equacao1)

    for eq in equacoes_com_x_isolado:
        derivada = calculaEExibeDerivada(eq, x)
    return equacoes_com_x_isolado


if __name__ == '__main__':
    intervalos = verificaIntervalo()

    funcao_continua = verificaFuncoes(intervalos)

    if funcao_continua:
        #if verificaDerivadaContinua(funcao_continua, intervalos):
            #print("A derivada é contínua em todos os intervalos encontrados.")
        iteracoes(funcao_continua, intervalos)
    else:
        print("\nNenhuma função contínua encontrada.")