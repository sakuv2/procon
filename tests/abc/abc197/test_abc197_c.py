# title: ORXOR
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_c

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.c import main


@pytest.mark.parametrize(
    "param",
    [
        Param(inputs=["3", "1 5 7"], outputs=["2"]),
        Param(inputs=["3", "10 10 10"], outputs=["0"]),
        Param(inputs=["4", "1 3 3 1"], outputs=["0"]),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
