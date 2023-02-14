from typing import List


class Polygon:
    def __init__(self, sides: List[float]) -> None:
        self.sides = sides

    def display_sides(self) -> List[float]:
        """
            Retorna a lista de lados.
        """
        return self.sides


class Triangle(Polygon):
    def find_area(self) -> float:
        """
            Calcula a área do triângulo.
        """
        a, b, c = self.sides
        side = (a + b + c) / 2
        area = (side*(side-a)*(side-b)*(side-c)) ** 0.5
        return area


triangle = Triangle([5, 6, 7])

print(f"----------------------")
print(f"Os lados do triângulo:")
print(*triangle.display_sides())
print(f"----------------------")
print(f"A área do triângulo é:")
print(f"{triangle.find_area():.2f}")
print(f"----------------------")
