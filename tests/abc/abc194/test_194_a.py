from unittest import mock

import pytest
from pydantic import BaseModel

from procon.abc.abc194.a import main


class Param(BaseModel):
    a: int
    b: int
    out: int

    def input(self):
        yield " ".join(map(str, [self.a, self.b]))


@pytest.mark.parametrize(
    "param",
    [
        Param(a=1, b=2, out=3),
        Param(a=0, b=0, out=4),
    ],
)
def test(param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        assert main() == param.out
