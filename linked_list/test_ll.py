import pytest

from linked_list import SinglyLL, DoublyLL

ITEMS: list[int] = [2, 9, 1, 0]


@pytest.fixture
def num_sll() -> SinglyLL:
    l: SinglyLL = SinglyLL()
    l.append_multiple(ITEMS)
    return l


@pytest.fixture
def num_dll() -> DoublyLL:
    l: DoublyLL = DoublyLL()
    l.append_multiple(ITEMS)
    return l


def test_sll_append(num_sll: SinglyLL):
    num_sll.append(5)

    as_str = ""
    for i in num_sll:
        as_str += str(i)
    assert as_str == "29105"


def test_sll_append_multiple(num_sll: SinglyLL):
    num_sll.append_multiple([5, 8, 3])

    as_str = ""
    for i in num_sll:
        as_str += str(i)
    assert as_str == "2910583"


def test_sll_insert_begin(num_sll: SinglyLL):
    num_sll.insert(5)

    as_str = ""
    for i in num_sll:
        as_str += str(i)
    assert as_str == "52910"


def test_sll_insert_middle(num_sll: SinglyLL):
    num_sll.insert(5, 3)

    as_str = ""
    for i in num_sll:
        as_str += str(i)
    assert as_str == "29150"


def test_sll_remove(num_sll: SinglyLL):
    num_sll.remove(9)

    as_str = ""
    for i in num_sll:
        as_str += str(i)
    assert as_str == "210"


def test_sll_find(num_sll: SinglyLL):
    for i in ITEMS:
        assert num_sll.find(i) is not None


def test_sll_contains(num_sll: SinglyLL):
    for i in ITEMS:
        assert num_sll.find(i)


def test_dll_append(num_dll: DoublyLL):
    num_dll.append(5)

    as_str = ""
    for i in num_dll:
        as_str += str(i)
    assert as_str == "29105"
