# title: Traveler
# problem link: https://atcoder.jp/contests/abc197/tasks/abc197_e

from unittest import mock

import pytest

from procon import Param
from procon.abc.abc197.e import main


@pytest.mark.parametrize(
    "param",
    [
        Param(inputs=["5", "2 2", "3 1", "1 3", "4 2", "5 3"], outputs=["12"]),
        Param(
            inputs=["9", "5 5", "-4 4", "4 3", "6 3", "-5 5", "-3 2", "2 2", "3 3", "1 4"],
            outputs=["38"],
        ),
    ],
)
def test(param: Param):
    inp = param.gen_inputs()
    with mock.patch("builtins.input", lambda: next(inp)):
        res = main()
        if not isinstance(res, list):
            res = [res]
        assert list(map(str, res)) == param.outputs
