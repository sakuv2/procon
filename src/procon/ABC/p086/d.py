# https://atcoder.jp/contests/abc086/tasks/arc089_b
from dataclasses import dataclass
from functools import cached_property
from itertools import product
from typing import List, Literal, Tuple


def get_values() -> Tuple[int, int, str]:
    x, y, c = input().split()
    return int(x), int(y), c


def get_inputs() -> Tuple[int, List[Tuple[int, int, str]]]:
    N, K = tuple(map(int, input().split()))
    return K, [get_values() for _ in range(N)]


@dataclass
class Ichimatsu:
    x: int
    y: int
    c: Literal["W", "B"]
    k: int

    @cached_property
    def rev_c(self):
        return "B" if self.c == "W" else "W"

    def color(self, x: int, y: int) -> Literal["W", "B"]:
        fx = ((x - self.x) // self.k) % 2 == 0
        fy = ((y - self.y) // self.k) % 2 == 0
        return self.c if fx ^ fy else self.rev_c

    def check(self, x: int, y: int, c: Literal["W", "B"]) -> bool:
        return self.color(x, y) == c


def main():
    K, steps = get_inputs()
    N = len(steps)
    max_count = 0
    for x, y, c in product(range(K), range(K), ["W", "B"]):
        ichimatsu = Ichimatsu(x, y, c, K)
        count = [ichimatsu.check(*step) for step in steps].count(True)
        max_count = count if count > max_count else max_count
        if max_count == N:
            break
    print(max_count)


if __name__ == "__main__":
    main()
