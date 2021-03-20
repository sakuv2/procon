from typing import List, Literal, Tuple
from unittest import mock

import pytest
from _pytest.capture import CaptureFixture
from pydantic import BaseModel

from procon.ABC.p086.d import main


class Param(BaseModel):
    N: int
    K: int
    steps: List[Tuple[int, int, Literal["B", "W"]]]
    out: str

    def input(self):
        yield " ".join([str(self.N), str(self.K)])
        yield from map(lambda step: " ".join(map(str, step)), self.steps)


@pytest.mark.parametrize(
    "param",
    [
        Param(N=4, K=3, steps=[(0, 1, "W"), (1, 2, "W"), (5, 3, "B"), (5, 4, "B")], out=4),
        Param(N=2, K=1000, steps=[(0, 0, "B"), (0, 1, "W")], out=2),
        Param(
            N=6,
            K=2,
            steps=[
                (1, 2, "B"),
                (2, 1, "W"),
                (2, 2, "B"),
                (1, 0, "B"),
                (0, 6, "W"),
                (4, 5, "W"),
            ],
            out=4,
        ),
    ],
)
def test(capfd: CaptureFixture, param: Param):
    inp = param.input()
    with mock.patch("builtins.input", lambda: next(inp)):
        main()
        out, _ = capfd.readouterr()
        assert param.out in out
