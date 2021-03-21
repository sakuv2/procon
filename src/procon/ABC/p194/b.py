# https://atcoder.jp/contests/abc194/tasks/abc194_b
from functools import reduce
from itertools import product
from typing import List, Tuple


def get_steps() -> Tuple[int, int]:
    a, b = map(int, input().split())
    return a, b


def get_input() -> List[Tuple[int, int]]:
    n = int(input())
    return [get_steps() for _ in range(n)]


def main() -> int:
    ab = get_input()
    n = len(ab)

    def f(i, j):
        a, b = ab[i][0], ab[j][1]
        return a + b if i == j else max(a, b)

    return reduce(lambda x, z: min(x, f(*z)), product(range(n), range(n)), 1e7)


if __name__ == "__main__":
    print(main())
