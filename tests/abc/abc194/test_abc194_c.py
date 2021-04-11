from typing import List
from unittest import mock

import pytest
from pydantic import BaseModel

from procon.abc.abc194.c import main


class Param(BaseModel):
    N: int
    arr: List[int]
    out: int

    def input(self):
        yield str(self.N)
        yield " ".join(map(str, self.arr))


@pytest.mark.parametrize(
    "param",
    [
        Param(N=3, arr=[2, 8, 4], out=56),
        Param(N=5, arr=[-5, 8, 9, -4, -3], out=950),
    ],
)
def test(param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert main() == param.out
