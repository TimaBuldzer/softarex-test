import dataclasses
from typing import Iterable, TypeVar, NamedTuple

height = TypeVar('height', int, str)
width = TypeVar('width', int, str)
np_array = TypeVar('np_array', Iterable, list)


@dataclasses.dataclass
class Dataset:
    train_x: np_array
    train_y: np_array
    test_x: np_array


class Dimensions(NamedTuple):
    height: int
    width: int
