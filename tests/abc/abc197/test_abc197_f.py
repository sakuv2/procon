# title: Construct a Palindrome
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_f

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.f import main


@pytest.mark.parametrize(
    "param",
    [
        Param(
            inputs=["8 8", "1 2 a", "2 3 b", "1 3 c", "3 4 b", "4 5 a", "5 6 c", "6 7 b", "7 8 a"],
            outputs=["10"],
        ),
        Param(inputs=["4 5", "1 1 a", "1 2 a", "2 3 a", "3 4 b", "4 4 a"], outputs=["5"]),
        Param(inputs=["3 4", "1 1 a", "1 2 a", "2 3 b", "3 3 b"], outputs=["-1"]),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
