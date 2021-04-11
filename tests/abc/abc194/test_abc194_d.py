from typing import List
from unittest import mock

import pytest
from pydantic import BaseModel

from procon.abc.abc194.d import main, my_main


class Param(BaseModel):
    N: int
    out: float

    def input(self):
        yield str(self.N)


@pytest.mark.parametrize(
    "param",
    [
        Param(N=2, out=2),
        Param(N=3, out=4.5),
    ],
)
def test(param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert main() == param.out
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert my_main() == param.out
