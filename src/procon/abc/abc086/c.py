# https://atcoder.jp/contests/abc086/tasks/arc089_a
from typing import List, Tuple


def get_values() -> Tuple[int, int, int]:
    return tuple(map(int, input().split()))


def get_steps() -> List[Tuple[int, int, int]]:
    return [get_values() for _ in range(int(input()))]


def check(before: Tuple[int, int, int], after: Tuple[int, int, int]) -> bool:
    bt, bx, by = before
    at, ax, ay = after
    manhattan = abs(ax - bx) + abs(ay - by)
    t = at - bt
    if manhattan > t:
        return False
    elif (t - manhattan) % 2 == 0:
        return True
    else:
        return False


def main():
    steps = [(0, 0, 0)] + get_steps()
    for i in range(len(steps) - 1):
        if not check(steps[i], steps[i + 1]):
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
