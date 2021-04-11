# title: Opposite
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_d

from math import cos, pi, sin
from typing import Union


def rotete(x, y, theta):
    _x = x * cos(theta) - y * sin(theta)
    _y = x * sin(theta) + y * cos(theta)
    return _x, _y


def main() -> Union[list, int, str]:
    n = int(input())
    x0, y0 = map(int, input().split())
    xh, yh = map(int, input().split())
    xm, ym = (x0 + xh) / 2, (y0 + yh) / 2
    theta = 2 * pi / n
    x, y = rotete(x0 - xm, y0 - ym, theta)

    return f"{x + xm:.11f} {y + ym:.11f}"


if __name__ == "__main__":
    res = main()
    if not isinstance(res, list):
        res = [res]
    [*map(print, res)]
