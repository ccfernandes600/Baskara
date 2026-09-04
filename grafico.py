from math import isfinite


def definir_intervalo_x(a, b, raizes):
    """Define uma janela que inclui as raizes e o vertice da parabola."""
    try:
        vertice_x = -b / (2 * a)
    except (ZeroDivisionError, OverflowError) as erro:
        raise ValueError("Nao foi possivel calcular o vertice para o grafico.") from erro

    referencias = [0.0, vertice_x, *raizes]
    if not all(isfinite(valor) for valor in referencias):
        raise ValueError("Nao ha valores finitos suficientes para desenhar o grafico.")

    limite = max(abs(valor) for valor in referencias)
    margem = max(2.0, limite * 0.5)
    return -limite - margem, limite + margem


def exibir_grafico(a, b, c, raizes):
    """Desenha a parabola e destaca suas raizes reais."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("\nGrafico nao exibido: instale matplotlib com 'pip install matplotlib'.")
        return

    try:
        inicio, fim = definir_intervalo_x(a, b, raizes)
        quantidade_pontos = 401
        passo = (fim - inicio) / (quantidade_pontos - 1)
        valores_x = [inicio + indice * passo for indice in range(quantidade_pontos)]
        valores_y = [a * x ** 2 + b * x + c for x in valores_x]
    except (OverflowError, ValueError, ZeroDivisionError) as erro:
        print(f"\nGrafico nao exibido: {erro}")
        return

    if not all(isfinite(valor) for valor in valores_y):
        print("\nGrafico nao exibido: a parabola possui valores nao finitos na escala calculada.")
        return

    try:
        plt.plot(valores_x, valores_y, label="f(x) = ax^2 + bx + c")
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)

        if raizes:
            plt.scatter(raizes, [0] * len(raizes), color="red", zorder=3, label="Raizes")

        plt.title("Grafico da parabola")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.show()
    except (RuntimeError, ValueError) as erro:
        print(f"\nGrafico nao exibido: {erro}")
