# Exercício
# Utilizar `reduce()`.
# Defina uma **função** chamada **weird_prod** que recebe como argumento uma lista de números inteiros e devolve o produto do primeiro elemento, pelo quadrado do segundo, pelo cubo do terceiro, e assim sucessivamente.

from typing import List
from functools import reduce


def weird_prod(numbers: List[int]) -> int:
    return reduce(lambda x, y: x * y, map(lambda x, i: x ** (i + 1), numbers, range(len(numbers))))


print(weird_prod([1, 2, 3]))


# Usando `for` ficaria deste modo:
#
# def weird_prod(nums: List[int]) -> int:
#    result = 1
#    length = len(nums)
#    for i in range(length):
#        result *= nums[i] ** (i + 1)
#        print(result)
#    return result
#
#print(weird_prod([5, 2, 4]))
