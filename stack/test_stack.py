import pytest

from stack import Stack

INITIAL_ITEMS = ["red", "blue", "green"]


@pytest.fixture
def color_stack() -> Stack:
    s: Stack = Stack()
    s.push_multiple(INITIAL_ITEMS)
    return s


def test_peek(color_stack: Stack):
    assert color_stack.peek() == INITIAL_ITEMS[-1]


def test_size(color_stack: Stack):
    assert color_stack.size() == len(INITIAL_ITEMS)


def test_push(color_stack: Stack):
    color_stack.push("yellow")
    assert color_stack.peek() == "yellow"


def test_pop(color_stack: Stack):
    assert color_stack.pop() == INITIAL_ITEMS[-1]


def test_push_multiple(color_stack: Stack):
    items = ["pink", "purple", "orange"]
    color_stack.push_multiple(items)

    for i in range(len(items)):
        assert color_stack.pop() == items[-(i + 1)]
