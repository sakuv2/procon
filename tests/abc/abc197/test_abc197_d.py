# title: Opposite
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_d

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.d import main


@pytest.mark.parametrize(
    "param",
    [
        Param(inputs=["4", "1 1", "2 2"], outputs=["2.00000000000 1.00000000000"]),
        Param(inputs=["6", "5 3", "7 4"], outputs=["5.93301270189 2.38397459622"]),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
