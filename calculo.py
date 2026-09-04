from math import isfinite, sqrt


def calcular_delta(a, b, c):
    """Calcula o discriminante e rejeita resultados nao representaveis."""
    try:
        delta = b ** 2 - 4 * a * c
    except OverflowError as erro:
        raise ValueError("Os coeficientes sao grandes demais para calcular o delta.") from erro

    if not isfinite(delta):
        raise ValueError("Os coeficientes produzem um delta nao finito.")

    return delta


def calcular_raizes(a, b, delta):
    """Calcula as raizes reais a partir do discriminante."""
    if a == 0:
        raise ValueError("O coeficiente a deve ser diferente de zero.")

    if delta < 0:
        return []

    try:
        denominador = 2 * a
        if denominador == 0 or not isfinite(denominador):
            raise ValueError("Nao foi possivel formar o denominador da formula de Bhaskara.")

        if delta == 0:
            raiz = -b / denominador
            if not isfinite(raiz):
                raise ValueError("A raiz calculada nao e finita.")
            return [raiz]

        raiz_delta = sqrt(delta)
        raiz_1 = (-b + raiz_delta) / denominador
        raiz_2 = (-b - raiz_delta) / denominador
    except (OverflowError, ValueError, ZeroDivisionError) as erro:
        raise ValueError("Nao foi possivel calcular as raizes reais.") from erro

    if not all(isfinite(raiz) for raiz in (raiz_1, raiz_2)):
        raise ValueError("As raizes calculadas nao sao finitas.")

    return [raiz_1, raiz_2]


def resolver_equacao(a, b, c):
    """Retorna o delta e as raizes reais da equacao."""
    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, delta)
    return delta, raizes
