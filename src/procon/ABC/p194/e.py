# https://atcoder.jp/contests/abc194/tasks/abc194_d
# https://atcoder.jp/contests/abc194/submissions/21141177
from typing import List


def get_input() -> List[int]:
    n, m = map(int, input().split())
    xs = map(int, input().split())
    return n, m, xs


def main() -> int:
    N, M, xs = get_input()
    xs = list(xs)

    cnt = [0] * (N + 1)
    for x in xs[:M]:
        cnt[x] += 1

    def update_mex(mex: int, a: int, b: int) -> int:
        cnt[a] -= 1
        cnt[b] += 1
        if cnt[a] == 0:
            mex = min(a, mex)
        return mex

    min_mex = cnt.index(0)
    for i in range(0, N - M):
        min_mex = update_mex(min_mex, xs[i], xs[i + M])

    return min_mex


if __name__ == "__main__":
    print(main())
