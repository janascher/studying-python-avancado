from typing import List


def get_user_words() -> List[str]:
    """
        Pede ao usuário para inserir uma lista de palavras separadas por vígulas.
    """
    words_input = input(
        "\nInsira a lista de palavras separadas por vírgula: ").split()
    return words_input


def count_x_occurrences(word: str) -> int:
    """
        Calcula a quantidade de vezes que a letra "x" ou "X" aparece em cada palavra inserida pelo usuário acima.
    """
    count_accurrences = word.count("x") + word.count("X")
    return count_accurrences


def inform_average(average: float) -> None:
    """
        Imprime uma mensagem ao usuário informando a médias de ocorrências da letra "x" de todas as palavras inseridas pelo usuário
    """
    print(f"\nA média de ocorrências da letra X é {average}")


def main():
    """
        Agrupa as funcções `get_user_words()`, `count_x_occurrence()` e `inform_average` para realizar as seguintes ações:
            - chama a função `get_user_words()` e armazena o resultado em `words_user`;
            - calcula a quantidade de ocorrências da letra "x" ou "X" em cada palavra usando a função `count_x_occurrences()` e armazena o resultado em `x_occurrences`;
            - calcula a média de ocorrências da letra "x" ou "X" em todas as palavras e armazena o resultado em `average`;
            - chama a função `inform_average()` informando a média calculada.
    """
    words_user = get_user_words()
    x_occurrences = [count_x_occurrences(word) for word in words_user]
    average = sum(x_occurrences) / 2
    inform_average(average)


if __name__ == "__main__":
    main()
