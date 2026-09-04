# Calculadora de Bhaskara

Projeto didático para resolver equações do segundo grau pela fórmula de Bhaskara:

```text
ax² + bx + c = 0
```

O programa solicita os coeficientes `a`, `b` e `c`, calcula o discriminante
(delta), apresenta as raízes reais e exibe o gráfico da parábola quando o
`matplotlib` estiver instalado.

## Objetivo pedagógico

Este projeto foi criado como exemplo para a disciplina de **Técnicas de
Programação**. A solução é organizada em múltiplos arquivos para demonstrar,
de forma prática, a separação de responsabilidades e a reutilização de
funções.

## Organização

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Coordena a execução do programa. |
| `entrada.py` | Lê e valida os coeficientes informados pelo usuário. |
| `calculo.py` | Calcula o delta e as raízes da equação. |
| `resultados.py` | Formata e mostra os resultados no terminal. |
| `grafico.py` | Desenha o gráfico da parábola. |

## Como executar

Com Python 3 instalado, execute:

```bash
python main.py
```

Para visualizar o gráfico, instale a dependência opcional:

```bash
pip install matplotlib
```
