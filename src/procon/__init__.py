__version__ = "0.1.0"

from dataclasses import dataclass
from typing import List


@dataclass
class Param:
    inputs: List[str]
    outputs: List[str]

    def gen_inputs(self):
        yield from self.inputs
