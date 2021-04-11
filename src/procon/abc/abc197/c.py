# title: ORXOR
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_c

from functools import reduce
from operator import or_
from typing import List, Union


def bit_or(xs: List[int]) -> int:
    return reduce(or_, xs, 0)


def main() -> Union[list, int, str]:
    n = int(input())
    xs = [*map(int, input().split())]

    m = 2 ** 30
    for i in range(2 ** n):
        xored = 0
        ored = 0
        for j in range(n + 1):
            if j < n:
                ored |= xs[j]
            if j == n or (i >> j) & 1:
                xored ^= ored
                ored = 0
        m = min(m, xored)
    return m


if __name__ == "__main__":
    res = main()
    if not isinstance(res, list):
        res = [res]
    [*map(print, res)]
