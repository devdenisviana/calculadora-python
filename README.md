# Calculadora em Python

Uma calculadora simples de linha de comando feita em Python, que realiza operações entre dois números inteiros.

## Funcionalidades

- Soma (+)
- Subtração (–)
- Multiplicação (×)
- Divisão (÷)
- Módulo / resto da divisão (%)

## Recursos

- Validação de entrada: só aceita números inteiros, pedindo novamente caso o usuário digite algo inválido.
- Validação da operação escolhida: aceita apenas opções de 1 a 5.
- Tratamento de divisão por zero: para as operações de divisão e módulo, o programa impede que o segundo número seja zero, solicitando um novo valor até que seja válido.

## Como executar

Certifique-se de ter o Python instalado. No Windows:

```bash
python calc.py
```

No Linux/Mac:

```bash
python3 calc.py
```

## Exemplo de uso

```
=== Calculadora ===
Digite o primeiro número inteiro: 10
Digite o segundo número inteiro: 5

Escolha a operação:
1 - Soma (+)
2 - Subtração (–)
3 - Multiplicação (×)
4 - Divisão (÷)
5 - Módulo (resto da divisão) (%)
Qual operação você deseja? Digite o número correspondente (1 a 5): 1

O resultado é: 15
```

## Tecnologias

- Python 3