# title: Rotate
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_a

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.a import main


@pytest.mark.parametrize(
    "param",
    [
        Param(inputs=["abc"], outputs=["bca"]),
        Param(inputs=["aab"], outputs=["aba"]),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
