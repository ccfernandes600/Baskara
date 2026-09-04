from calculo import resolver_equacao
from entrada import ler_coeficientes
from grafico import exibir_grafico
from resultados import imprimir_resultados


def main():
    coeficientes = ler_coeficientes()
    if coeficientes is None:
        return

    a, b, c = coeficientes

    try:
        delta, raizes = resolver_equacao(a, b, c)
    except ValueError as erro:
        print(f"\nNao foi possivel resolver a equacao: {erro}")
        return

    imprimir_resultados(a, b, c, delta, raizes)
    exibir_grafico(a, b, c, raizes)


if __name__ == "__main__":
    main()
