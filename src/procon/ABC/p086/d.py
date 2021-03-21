# https://atcoder.jp/contests/abc086/tasks/arc089_b
# https://atcoder.jp/contests/abc086/submissions/21125672
from functools import reduce
from itertools import product
from typing import List, Tuple


def get_values() -> Tuple[int, int, int]:
    x, y, c = input().split()
    return int(x), int(y), int(c == "W")


def get_inputs() -> Tuple[int, List[Tuple[int, int, int]]]:
    N, K = map(int, input().split())
    return K, [get_values() for _ in range(N)]


def main() -> int:
    k, steps = get_inputs()

    g = [[[0] * k for _ in range(k)] for _ in range(2)]
    for step in steps:
        x, y, c = step
        x, y = x % (2 * k), y % (2 * k)
        c = 1 - c if (x < k) ^ (y < k) else c
        x, y = x if x < k else x - k, y if y < k else y - k
        g[c][x][y] += 1

    cs = [[[0] * (k + 1) for _ in range(k + 1)] for _ in range(2)]
    for x, y, c in product(range(k), range(k), (0, 1)):
        cs[c][x + 1][y + 1] = cs[c][x + 1][y] + cs[c][x][y + 1] - cs[c][x][y] + g[c][x][y]

    s = lambda c, x, y: (
        cs[c][k][k]
        - cs[c][x][k]
        - cs[c][k][y]
        + 2 * cs[c][x][y]
        + cs[1 - c][x][k]
        + cs[1 - c][k][y]
        - 2 * cs[1 - c][x][y]
    )

    return reduce(lambda x, z: max(x, s(*z)), product(range(2), range(k), range(k)), 0)


if __name__ == "__main__":
    print(main())
