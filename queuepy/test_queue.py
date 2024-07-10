import pytest

from . import Queue

ITEMS: list[str] = ["red", "blue", "green"]


@pytest.fixture
def color_queue() -> Queue:
    s: Queue = Queue()
    s.enqueue_multiple(ITEMS)
    return s


def test_peek(color_queue: Queue):
    assert color_queue.peek() == ITEMS[0]


def test_enqueue(color_queue: Queue):
    color_queue.enqueue("yellow")
    assert color_queue.items[-1] == "yellow"


def test_enqueue_multiple(color_queue: Queue):
    more_items = ["yellow", "purple"]
    color_queue.enqueue_multiple(more_items)
    assert color_queue.items[-len(more_items) :] == more_items


def test_dequeue(color_queue: Queue):
    assert color_queue.dequeue() == ITEMS[0]


def test_size(color_queue: Queue):
    assert color_queue.size() == len(ITEMS)
