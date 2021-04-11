# title: Visibility
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_b

from typing import List, Union


def main() -> Union[List, int, str]:
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    tate = []
    yoko = []
    for i in range(h):
        row = list(map(lambda x: x == ".", input()))
        tate.append(row[y])
        if i == x:
            yoko = row

    up = range(x - 1, -1, -1)
    down = range(x + 1, h, 1)
    left = range(y - 1, -1, -1)
    right = range(y + 1, w, 1)
    res = 1 if tate[x] else 0

    for r in [up, down]:
        for i in r:
            if tate[i]:
                res += 1
            else:
                break
    for r in [left, right]:
        for i in r:
            if yoko[i]:
                res += 1
            else:
                break

    return res


if __name__ == "__main__":
    res = main()
    if not isinstance(res, list):
        res = [res]
    [*map(print, res)]
