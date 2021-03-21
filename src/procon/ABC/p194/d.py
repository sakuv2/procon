# https://atcoder.jp/contests/abc194/tasks/abc194_d
from typing import List


def get_input() -> List[int]:
    n = int(input())
    return n


def my_main() -> int:
    n = get_input()

    def exp(n, m):
        e = 0
        p, q = 1 - m / n, m / n
        i = 0
        while True:
            i += 1
            new = i * q ** (i - 1) * p
            if new < 1e-7:
                break
            e += new
        return e

    ans = sum([exp(n, i) for i in range(1, n)])
    return round(ans, 6)


def main():
    n = get_input()
    return n * sum([1 / x for x in range(1, n)])


if __name__ == "__main__":
    print(main())
