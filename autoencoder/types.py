import dataclasses
from typing import Iterable, TypeVar, NamedTuple

height = TypeVar('height', int, str)
width = TypeVar('width', int, str)
np_array = TypeVar('np_array', Iterable, list)


class Dataset(NamedTuple):
    train_x: np_array
    train_y: np_array
    test_x: np_array


@dataclasses.dataclass
class Dimensions:
    height: int
    width: int
