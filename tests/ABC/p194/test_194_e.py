from typing import List
from unittest import mock

import pytest
from pydantic import BaseModel

from procon.ABC.p194.e import main


class Param(BaseModel):
    N: int
    M: int
    arr: List[int]
    out: float

    def input(self):
        yield " ".join(map(str, [self.N, self.M]))
        yield " ".join(map(str, self.arr))


@pytest.mark.parametrize(
    "param",
    [
        Param(N=3, M=2, arr=[0, 0, 1], out=1),
        Param(N=3, M=2, arr=[1, 1, 1], out=0),
        Param(N=3, M=2, arr=[0, 1, 0], out=2),
        Param(N=7, M=3, arr=[0, 0, 1, 2, 0, 1, 0], out=2),
    ],
)
def test(param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert main() == param.out
