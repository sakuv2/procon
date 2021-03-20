from typing import List, Tuple
from unittest import mock

import pytest
from _pytest.capture import CaptureFixture
from pydantic import BaseModel

from procon.ABC.p086.c import main


class Param(BaseModel):
    N: int
    steps: List[Tuple[int, int, int]]
    out: str

    def input(self):
        yield str(self.N)
        yield from map(lambda step: " ".join(map(str, step)), self.steps)


@pytest.mark.parametrize(
    "param",
    [
        Param(N=2, steps=[(3, 1, 2), (6, 1, 1)], out="Yes"),
        Param(N=1, steps=[(2, 100, 100)], out="No"),
        Param(N=2, steps=[(5, 1, 1), (100, 1, 1)], out="No"),
    ],
)
def test(capfd: CaptureFixture, param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        main()
        out, _ = capfd.readouterr()
        assert param.out in out
