# https://atcoder.jp/contests/abc086/tasks/arc089_b
# https://atcoder.jp/contests/abc086/submissions/21124856
from itertools import product
from typing import List, Tuple


def get_values() -> Tuple[int, int, int]:
    x, y, c = input().split()
    return int(x), int(y), int(c == "W")


def get_inputs() -> Tuple[int, List[Tuple[int, int, int]]]:
    N, K = map(int, input().split())
    return K, [get_values() for _ in range(N)]


def main():
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

    ans = 0
    for x, y in product(range(k), range(k)):
        ans = max(
            cs[0][k][k]
            - cs[0][x][k]
            - cs[0][k][y]
            + 2 * cs[0][x][y]
            + cs[1][x][k]
            + cs[1][k][y]
            - 2 * cs[1][x][y],
            cs[1][k][k]
            - cs[1][x][k]
            - cs[1][k][y]
            + 2 * cs[1][x][y]
            + cs[0][x][k]
            + cs[0][k][y]
            - 2 * cs[0][x][y],
            ans,
        )
    print(ans)


if __name__ == "__main__":
    main()
