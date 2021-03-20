# https://atcoder.jp/contests/abc086/tasks/abc086_b
from typing import Tuple


def get_values() -> Tuple[int, int]:
    return tuple(map(int, input().split()))


def main():
    a, b = get_values()

    x = int(f"{a}{b}")
    if (x ** 0.5) % 1 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
