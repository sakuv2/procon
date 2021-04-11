# https://atcoder.jp/contests/abc086/tasks/abc086_a
from typing import Tuple


def get_values() -> Tuple[int, int]:
    return tuple(map(int, input().split()))


def main():
    a, b = get_values()

    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
