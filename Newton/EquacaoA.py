import sympy as sp
import numpy as np

def retornoFuncao(x):
    resultado = 2 * x**3 - 6 * x - 1
    return resultado

def retornoDerivada(valor):
    x = sp.symbols('x')
    derivada = calculaEExibeDerivada()
    resultado = derivada.subs(x, valor)
    return resultado

def verificaContinuidade(funcao, intervalo):
    x = sp.symbols('x')

    # Define a função simbólica
    f = sp.sympify(funcao)

    # Verifica se o denominador da função é zero
    denominador = f.as_numer_denom()[1]
    pontos_criticos = sp.solve(denominador, x)

    # Verifica se os pontos críticos estão dentro do intervalo
    pontos_dentro_do_intervalo = [p for p in pontos_criticos if intervalo[0] <= p <= intervalo[1]]

    if pontos_dentro_do_intervalo:
        print(f"A função não é contínua nos seguintes pontos críticos: {pontos_dentro_do_intervalo}")
        return False
    else:
        print(f"A função é contínua no intervalo [{intervalo[0]}, {intervalo[1]}].")
        return True


def verificaDerivadaContinua(funcao, intervalos):
    x = sp.symbols('x')

    # Calcula a derivada da função
    derivada = sp.diff(funcao, x)
    print(f"A derivada da f(X) é: {derivada}")

    for intervalo in intervalos:
        print(f"Calculando a continuidade da derivada para o intervalo: [{intervalo[0]},{intervalo[1]}]...")
        continua = True  # Inicialmente, assumimos que a derivada é contínua no intervalo

        for ponto in np.linspace(float(intervalo[0]), float(intervalo[1]), 100):
            limite_esquerda = sp.limit(derivada, x, ponto, dir='-')
            limite_direita = sp.limit(derivada, x, ponto, dir='+')
            valor_ponto = derivada.subs(x, ponto)

            if limite_esquerda != limite_direita != valor_ponto:
                print(f"A derivada não é contínua em x = {ponto} no intervalo {intervalo}")
                continua = False  # A derivada não é contínua no intervalo
                break  # Pode parar de verificar, pois já sabemos que não é contínua

        if continua:
            print(f"A derivada é contínua no intervalo [{intervalo[0]},{intervalo[1]}].")
        else:
            print(f"A derivada não é contínua no intervalo [{intervalo[0]},{intervalo[1]}].")

    return continua


def verificaDerivadaIgualAZero(derivada, intervalos):
    x = sp.symbols('x')

    for intervalo in intervalos:
        print(f"Calculando se há um número onde a derivada da f(x) é igual a zero no intervalo: [{intervalo[0]},{intervalo[1]}]...")
        for ponto in np.linspace(intervalo[0], intervalo[1], 100):
            valor_ponto = derivada.subs(x, ponto)
            if abs(valor_ponto) == 0:
                print(f"Derivada é igual a 0 em x = {ponto} no intervalo {intervalo}...")
                break
    print("-------------------------------------------------------------")
    return True

def verificaFuncoes(intervalos):
    x = sp.symbols('x')
    funcoes = modificaFuncao()

    funcao_continua = None

    for eq in funcoes:
        print(f"f(X) sendo análisada... {eq}")
        for intervalo in intervalos:
            if verificaContinuidade(eq, intervalo):
                print(f"A f(X): {eq} É contínua no intervalo [{intervalo[0]}, {intervalo[1]}].")
                funcao_continua = eq
    print("------------------------------------------------------------------------------------")

    if funcao_continua:
        if verificaDerivadaContinua(funcao_continua, intervalos):  # Verifique a derivada no primeiro intervalo
            print(f"A derivada também é contínua para todos os intervalo.")
            print("------------------------------------------------------------------------------------")
            derivada = sp.diff(funcao_continua, x)
            verificaDerivadaIgualAZero(derivada, intervalos)
            return funcao_continua
    else:
        print("\nNenhuma função contínua encontrada.")

    return funcao_continua


def iteracoes(funcao_continua, intervalos):
    cont = 1
    convergencia = 0
    x = sp.symbols('x')
    epsilon = 0.0000001

    for intervalo in intervalos:
        x0 = (intervalo[0] + intervalo[1]) / 2  # Ponto médio do intervalo
        derivada = sp.diff(funcao_continua, x)
        xk_anterior = x0
        xk = xk_anterior - (funcao_continua.subs(x, xk_anterior) / derivada.subs(x, xk_anterior))

        while abs(xk - xk_anterior) > epsilon:
            xk_anterior = xk
            xk = xk_anterior - (funcao_continua.subs(x, xk_anterior) / derivada.subs(x, xk_anterior))
            cont = cont + 1
        raiz = xk

        print("------------------------------------------------------------------------------------")
        print(f"Raiz encontrada no intervalo [{intervalo[0]}, {intervalo[1]}]: {raiz}")
        print(f"Quantidade de iterações necessárias: {cont}")



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
    equacao1 = 2 * x**3 - 6 * x - 1
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