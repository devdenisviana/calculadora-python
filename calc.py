"""
Calculadora simples em Python
Operações: soma, subtração, multiplicação, divisão e módulo.
"""


def ler_inteiro(mensagem):
    """Pede um número inteiro ao usuário, validando a entrada."""
    while True:
        entrada = input(mensagem)
        try:
            return int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_opcao():
    """Mostra o menu de operações e valida a escolha do usuário."""
    print("\nEscolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (–)")
    print("3 - Multiplicação (×)")
    print("4 - Divisão (÷)")
    print("5 - Módulo (resto da divisão) (%)")

    while True:
        entrada = input("Qual operação você deseja? Digite o número correspondente (1 a 5): ")
        try:
            opcao = int(entrada)
            if 1 <= opcao <= 5:
                return opcao
            else:
                print("Opção inválida. Escolha um número entre 1 e 5.")
        except ValueError:
            print("Opção inválida. Escolha um número entre 1 e 5.")


def ler_num2_nao_zero():
    """Pede um segundo número garantindo que seja diferente de zero
    (usado nas operações de divisão e módulo)."""
    num2 = ler_inteiro("Digite o segundo número inteiro: ")
    while num2 == 0:
        print("Erro: não é possível dividir por zero. Digite outro número diferente de zero.")
        num2 = ler_inteiro("Digite o segundo número inteiro: ")
    return num2


def calcular(opcao, num1, num2):
    """Executa a operação escolhida e retorna o resultado."""
    if opcao == 1:
        return num1 + num2
    elif opcao == 2:
        return num1 - num2
    elif opcao == 3:
        return num1 * num2
    elif opcao == 4:
        return num1 / num2
    elif opcao == 5:
        return num1 % num2


def main():
    print("=== Calculadora ===")

    num1 = ler_inteiro("Digite o primeiro número inteiro: ")
    opcao = ler_opcao()

    if opcao in (4, 5):
        num2 = ler_num2_nao_zero()
    else:
        num2 = ler_inteiro("Digite o segundo número inteiro: ")

    resultado = calcular(opcao, num1, num2)
    print(f"\nO resultado é: {resultado}")


if __name__ == "__main__":
    main()