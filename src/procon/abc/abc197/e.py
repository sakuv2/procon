# title: Traveler
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_e

from collections import defaultdict
from typing import Union


def main() -> Union[list, int, str]:
    n = int(input())

    dd = defaultdict(lambda: (int(1e9), -int(1e9)))
    for _ in range(n):
        x, c = map(int, input().split())
        dd[c] = (min(dd[c][0], x), max(dd[c][1], x))

    xl, xr, cl, cr = 0, 0, 0, 0
    for _, lr in sorted(dd.items()) + [(0, (0, 0))]:
        ml, mr = lr
        # 左端で終わる (ml < xl <= mr) or (ml < mr < xl)
        _cl = min(
            ((mr - xl) + (mr - ml) if xl <= mr else xl - ml) + cl,
            ((mr - xr) + (mr - ml) if xr <= mr else xr - ml) + cr,
        )
        # 右端で終わる (ml <= xr < mr) or (xr < ml < mr)
        _cr = min(
            ((xr - ml) + (mr - ml) if ml <= xr else mr - xr) + cr,
            ((xl - ml) + (mr - ml) if ml <= xl else mr - xl) + cl,
        )
        xl, xr, cl, cr = ml, mr, _cl, _cr
    return min(cr, cl)


if __name__ == "__main__":
    res = main()
    if not isinstance(res, list):
        res = [res]
    [*map(print, res)]
