# https://atcoder.jp/contests/abc194/tasks/abc194_a

from typing import Tuple


def get_input() -> Tuple[int, int]:
    a, b = map(int, input().split())
    return a, b


def main() -> int:
    a, b = get_input()

    if a + b >= 15 and b >= 8:
        return 1
    elif a + b >= 10 and b >= 3:
        return 2
    elif a + b >= 3:
        return 3
    else:
        return 4


if __name__ == "__main__":
    print(main())
