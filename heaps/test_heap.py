import pytest

from . import MaxHeap
from . import MinHeap

ITEMS: list[int] = [5, 2, 3, 6, 1, 8, 4, 7]


@pytest.fixture
def minhp() -> MinHeap:
    m: MinHeap = MinHeap()
    m.insert_multiple(ITEMS)
    return m


@pytest.fixture
def maxhp() -> MaxHeap:
    m: MaxHeap = MaxHeap()
    m.insert_multiple(ITEMS)
    return m


def test_min_get(minhp: MinHeap):
    assert minhp.get_min() == 1


def test_min_extract(minhp: MinHeap):
    assert minhp.extract_min() == 1
    assert minhp.get_min() == 2


def test_min_insert(minhp: MinHeap):
    minhp.insert(-1)
    assert minhp.get_min() == -1

    minhp.insert(10)
    assert minhp.get_min() == -1


def test_max_get(maxhp: MaxHeap):
    assert maxhp.get_max() == 8


def test_max_extract(maxhp: MaxHeap):
    assert maxhp.extract_max() == 8
    assert maxhp.get_max() == 7


def test_max_insert(maxhp: MaxHeap):
    maxhp.insert(10)
    assert maxhp.get_max() == 10

    maxhp.insert(0)
    assert maxhp.get_max() == 10
