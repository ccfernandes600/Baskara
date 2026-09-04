from math import isfinite


def ler_coeficiente(nome):
    """Le um coeficiente numerico e finito."""
    while True:
        try:
            texto = input(f"Informe o coeficiente {nome}: ").strip().replace(",", ".")
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada cancelada pelo usuario.")
            return None

        if not texto:
            print("Informe um valor.")
            continue

        try:
            valor = float(texto)
        except ValueError:
            print("Valor inválido. Digite um número, como 2,5 ou -3.")
            continue

        if not isfinite(valor):
            print("O valor precisa ser um numero finito.")
            continue

        return valor


def ler_coeficientes():
    """Le os coeficientes de uma equacao do segundo grau."""
    print("Equacao do segundo grau: ax^2 + bx + c = 0")

    while True:
        a = ler_coeficiente("a")
        if a is None:
            return None
        if a != 0:
            break
        print("O coeficiente a deve ser diferente de zero.")

    b = ler_coeficiente("b")
    if b is None:
        return None

    c = ler_coeficiente("c")
    if c is None:
        return None

    return a, b, c
