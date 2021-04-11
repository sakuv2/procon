# title: Rotate
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_a

from typing import List


def main() -> List[str]:
    txt = input()
    res = txt[1:] + txt[0]
    return [str(res)]


if __name__ == "__main__":
    [*map(print, main())]
