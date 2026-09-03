from math import sqrt


def ler_coeficiente(nome):
    return float(input(f"Informe o coeficiente {nome}: "))


def resolver_equacao(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return delta, []

    if delta == 0:
        return delta, [-b / (2 * a)]

    raiz_delta = sqrt(delta)
    return delta, [
        (-b + raiz_delta) / (2 * a),
        (-b - raiz_delta) / (2 * a),
    ]


def main():
    print("Equacao do segundo grau: ax^2 + bx + c = 0")
    a = ler_coeficiente("a")

    while a == 0:
        print("O coeficiente a deve ser diferente de zero.")
        a = ler_coeficiente("a")

    b = ler_coeficiente("b")
    c = ler_coeficiente("c")
    delta, raizes = resolver_equacao(a, b, c)

    print(f"Delta: {delta}")

    if not raizes:
        print("A equacao nao possui raizes reais.")
    elif len(raizes) == 1:
        print(f"Raiz unica: {raizes[0]}")
    else:
        print(f"Raiz 1: {raizes[0]}")
        print(f"Raiz 2: {raizes[1]}")


if __name__ == "__main__":
    main()
