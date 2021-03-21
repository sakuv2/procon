# https://atcoder.jp/contests/abc194/tasks/abc194_c
from typing import List


def get_array() -> List[int]:
    return list(map(int, input().split()))


def get_input() -> List[int]:
    n = int(input())
    return n, get_array()


def main() -> int:
    n, a = get_input()
    return n * sum(map(lambda x: x ** 2, a)) - sum(a) ** 2


if __name__ == "__main__":
    print(main())
