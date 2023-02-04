from typing import Generator

def count_up(x: int) -> Generator[int, None, None]:
    n = 1
    i = 0
    while n < x:
        yield n
        i += 1
        n += i

for num in count_up(70):
    print(num)