from typing import List, Tuple
from unittest import mock

import pytest
from pydantic import BaseModel

from procon.abc.abc194.b import main


class Param(BaseModel):
    N: int
    steps: List[Tuple[int, int]]
    out: int

    def input(self):
        yield str(self.N)
        yield from map(lambda x: " ".join(map(str, x)), self.steps)


@pytest.mark.parametrize(
    "param",
    [
        Param(N=3, steps=[(8, 5), (4, 4), (7, 9)], out=5),
        Param(N=3, steps=[(11, 7), (3, 2), (6, 7)], out=5),
    ],
)
def test(param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert main() == param.out
