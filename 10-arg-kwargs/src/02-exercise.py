from typing import List


def get_numbers() -> List[int]:
    """
        Solicita a entrada do usuário, converte a entrada de strings em inteiro e retorna uma lista de números.
    """
    numbers_input = input(
        "\nInsira uma lista de números separados por espaços: ")
    numbers_str = numbers_input.split()
    list_numbers = []
    for i in numbers_str:
        number = int(i)
        list_numbers.append(number)
    return list_numbers


def calculation_multiplication(*nums: int) -> int:
    """
        Recebe uma quantidade ilimitada de números inteiros e multiplica todos eles, retornando o resultado.
    """
    result = 1
    for i in nums:
        result *= i
    return result


def inform_multiplication(multiply: int) -> None:
    """
        Imprime o resultado da multiplicação dos números.
    """
    print(f"\nO resultado da multiplicação é {multiply}.")


def main():
    """
        Chama as três funções. Deste modo, obtem-se a entrada do usuário, multiplica os números e imprime o resultado.
    """
    number_user = get_numbers()
    result = calculation_multiplication(*number_user)
    inform_multiplication(result)


if __name__ == "__main__":
    """
        É uma verificação de segurança padrão em Python que garante que o código dentro do bloco `if` será executado apenas quando o arquivo for executado como um script principal.
    """
    main()
