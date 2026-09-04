def formatar_numero(numero):
    """Formata numeros sem exibir casas decimais desnecessarias."""
    return f"{numero:.6g}"


def imprimir_resultados(a, b, c, delta, raizes):
    """Exibe a equacao, o delta e suas raizes reais."""
    print("\n--- Resultados ---")
    print(
        f"Equacao: ({formatar_numero(a)})x^2 + "
        f"({formatar_numero(b)})x + ({formatar_numero(c)}) = 0"
    )
    print(f"Delta: {formatar_numero(delta)}")

    if delta < 0:
        print("A equacao nao possui raizes reais.")
    elif len(raizes) == 1:
        print(f"Raiz unica: x = {formatar_numero(raizes[0])}")
    else:
        print(f"Raiz 1: x1 = {formatar_numero(raizes[0])}")
        print(f"Raiz 2: x2 = {formatar_numero(raizes[1])}")
