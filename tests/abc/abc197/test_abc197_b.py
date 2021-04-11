# title: Visibility
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_b

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.b import main


@pytest.mark.parametrize(
    "param",
    [
        Param(inputs=["4 4 2 2", "##..", "...#", "#.#.", ".#.#"], outputs=["4"]),
        Param(inputs=["3 5 1 4", "#....", "#####", "....#"], outputs=["4"]),
        Param(inputs=["5 5 4 2", ".#..#", "#.###", "##...", "#..#.", "#.###"], outputs=["3"]),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
